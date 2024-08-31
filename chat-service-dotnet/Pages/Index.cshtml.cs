using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace chat_service_dotnet.Pages;

public class Index : PageModel
{
    private readonly ChatService _chat;
    [BindProperty]
    public CancellationToken cancellationToken { get; set; }

    [BindProperty]
    public string Prompt { get; set; } = default!;

    public Index(ChatService chat)
    {
        _chat = chat;
    }

    public async Task<IActionResult> OnPostAsync()
    {
        if (string.IsNullOrEmpty(Prompt))
        {
            throw new ArgumentException("Prompt is required");
        }

        var completion = await _chat.GetCompletion(Prompt, cancellationToken);

        return new RedirectToPageResult("/chat", new { prompt = Prompt, completion = completion.Content[0].Text });
    }
}
