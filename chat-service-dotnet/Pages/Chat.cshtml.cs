using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace chat_service_dotnet.Pages;

public class Chat : PageModel
{
    [BindProperty]
    public string? Prompt { get; set; }

    [BindProperty]
    public string? Completion { get; set; }

    [BindProperty]
    public CancellationToken CancellationToken { get; set; }

    public void OnGet()
    {
        Prompt = Request.Query["prompt"];
        Completion = Request.Query["completion"];
    }
}
