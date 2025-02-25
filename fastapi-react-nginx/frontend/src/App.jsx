import { useState } from "react";

function App() {
  const [inputText, setInputText] = useState("");
  const [length, setLength] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch("/api/length/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: inputText }),
    });
    const data = await response.json();
    setLength(data.length);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>字符串长度计算</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          placeholder="输入字符串"
        />
        <button type="submit">提交</button>
      </form>
      {length !== null && <p>字符串长度: {length}</p>}
    </div>
  );
}

export default App;
