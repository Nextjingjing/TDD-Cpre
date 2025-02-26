import { useEffect, useState } from "react";
import notes from "./data/data";
import NoteItem from "./components/NoteItem";

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    setData(notes);
  }, []);

  return (
    <>
      {data.map((note, index) => (
        <NoteItem key={index} note={note} />
      ))}
    </>
  );
}

export default App;
