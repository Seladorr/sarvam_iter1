import React, { useState } from 'react';
import axios from 'axios';

function Chat() {
  // In a real system, user IDs would be generated uniquely per user.
  const [userId] = useState("user123");
  const [message, setMessage] = useState("");
  const [conversation, setConversation] = useState([]);

  const handleSend = async () => {
    if (!message.trim()) return;
    
    // Add user's message to the chat history
    setConversation(prev => [...prev, { sender: "user", text: message }]);

    try {
      const response = await axios.post('http://localhost:5000/chat', {
        user_id: userId,
        message: message
      });
      const botResponse = response.data.response;
      setConversation(prev => [...prev, { sender: "bot", text: botResponse }]);
      setMessage("");
    } catch (error) {
      console.error("Error sending message", error);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-history">
        {conversation.map((msg, index) => (
          <div key={index} className={msg.sender === "user" ? "user-message" : "bot-message"}>
            <strong>{msg.sender}:</strong> {msg.text}
          </div>
        ))}
      </div>
      <div className="chat-input">
        <input 
          type="text"
          value={message}
          onChange={e => setMessage(e.target.value)}
          placeholder="Type your message..."
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
}

export default Chat;
