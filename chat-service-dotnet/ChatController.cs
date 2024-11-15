﻿using Microsoft.AspNetCore.Mvc;
using OpenAI.Chat;

namespace chat_service_dotnet;

[Route("[controller]")]
[ApiController]
public class ChatController : ControllerBase
{
    private readonly ChatService _chat;
    public ChatController(ChatService chat)
    {
        _chat = chat;
    }

    [HttpPost]
    [Produces("application/json")]
    public async Task<ChatCompletion> CreateCompletion([FromQuery]string prompt, CancellationToken cancellationToken)
    {
        return (await _chat.GetCompletion(prompt, cancellationToken)).Value;
    }
}
