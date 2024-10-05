using System.ClientModel;
using OpenAI.Chat;

namespace chat_service_dotnet;

public class ChatService
{
    private readonly ChatClient _chatClient;

    public ChatService(ChatClient chatClient)
    {
        _chatClient = chatClient;
    }

    public Task<ClientResult<ChatCompletion>> GetCompletion(string prompt, CancellationToken cancellationToken)
    {
        var message = ChatMessage.CreateUserMessage(prompt);
        return _chatClient.CompleteChatAsync([message], cancellationToken: cancellationToken);
    }
}
