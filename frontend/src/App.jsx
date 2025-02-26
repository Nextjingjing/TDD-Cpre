import { useEffect, useState } from "react";
import NoteItem from "./components/NoteItem";
import axios from "axios";

function App() {
  const [data, setData] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [searchFields, setSearchFields] = useState(["name", "tags"]); // ฟิลด์ที่ใช้ค้นหา

  useEffect(() => {
    const fetchData = async () => {
      try {
        const fieldsQuery = searchFields.map((field) => `field=${field}`).join("&");
        const url = searchQuery
          ? `http://127.0.0.1:8000/api/notes/?q=${searchQuery}&${fieldsQuery}`
          : "http://127.0.0.1:8000/api/notes/";

        const response = await axios.get(url);
        setData(response.data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, [searchQuery, searchFields]);

  return (
    <div>
      {/* ช่องค้นหา */}
      <input
        type="text"
        placeholder="ค้นหาโน้ต..."
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
      />

      {/* ตัวเลือกฟิลด์ค้นหา */}
      <div>
        <label>
          <input
            type="checkbox"
            checked={searchFields.includes("name")}
            onChange={() =>
            setSearchFields((prev) =>
              prev.includes("name") ? prev.filter(f => f !== "name") : [...prev, "name"]
            )}
          />
          ค้นหาจากชื่อ
        </label>

        <label>
          <input
            type="checkbox"
            checked={searchFields.includes("tags")}
            onChange={() =>
            setSearchFields((prev) =>
              prev.includes("tags") ? prev.filter(f => f !== "tags") : [...prev, "tags"]
            )}
          />
          ค้นหาจากแท็ก
        </label>
      </div>

      {/* แสดงรายการโน้ตที่ค้นพบ */}
      {data.length > 0 ? (
        data.map((note, index) => <NoteItem key={index} note={note} />)
      ) : (
        <p>ไม่พบโน้ตที่ค้นหา</p>
      )}
    </div>
  );
}

export default App;
