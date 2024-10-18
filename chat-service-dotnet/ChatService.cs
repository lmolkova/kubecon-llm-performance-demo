using System.ClientModel;
using System.ClientModel.Primitives;
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
        var system = ChatMessage.CreateSystemMessage("You're a helpful assistant. Keep your answers short.");
        var message = ChatMessage.CreateUserMessage(prompt);
        var options =  ModelReaderWriter.Read<ChatCompletionOptions>(BinaryData.FromString("{\"temperature\":1.0,\"max_tokens\":100}"));
        return _chatClient.CompleteChatAsync([system, message], options, cancellationToken: cancellationToken);
    }
}
