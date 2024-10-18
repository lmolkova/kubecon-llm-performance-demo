using chat_service_dotnet;
using Microsoft.Extensions.Options;
using OpenAI;
using OpenAI.Chat;
using OpenTelemetry.Logs;
using OpenTelemetry.Metrics;
using OpenTelemetry.Trace;
using System.ClientModel;

AppContext.SetSwitch("OpenAI.Experimental.EnableOpenTelemetry", true);

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddOpenTelemetry()
    .WithTracing(b =>
        b.AddSource("OpenAI*")
        .AddHttpClientInstrumentation()
        .AddAspNetCoreInstrumentation()
        .AddOtlpExporter())
    .WithMetrics(b =>
        b.AddMeter("OpenAI*")
        .AddView("gen_ai.client.operation.duration", new ExplicitBucketHistogramConfiguration {
            Boundaries = [0.01, 0.02, 0.04, 0.08, 0.16, 0.32, 0.64, 1.28, 2.56, 5.12,10.24, 20.48, 40.96, 81.92]})
        .AddHttpClientInstrumentation()
        .AddAspNetCoreInstrumentation()
        .AddOtlpExporter()
        .AddPrometheusExporter());

builder.Logging.AddOpenTelemetry(o =>
{
    o.ParseStateValues = true;
    o.IncludeScopes = true;
    o.AddOtlpExporter();
});

builder.Services.Configure<OpenAIOptions>(builder.Configuration.GetSection("OpenAI"));
builder.Services.AddSingleton(s => {
    var options = s.GetRequiredService<IOptions<OpenAIOptions>>();
    return new ChatClient(options.Value.Model, new ApiKeyCredential(options.Value.ApiKey), new OpenAIClientOptions()
    {
        Endpoint = options.Value.Endpoint,
    });
});
builder.Services.AddSingleton<ChatService>();
builder.Services.AddRazorPages();
builder.Services.AddControllers();

var app = builder.Build();
app.UseOpenTelemetryPrometheusScrapingEndpoint();
app.UseRouting();

app.MapRazorPages();
app.MapControllers();

app.Run();

class OpenAIOptions
{
    public string Model { get; set; }
    public Uri Endpoint { get; set; }
    public string ApiKey { get; set; }
}