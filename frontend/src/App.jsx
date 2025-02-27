import { useEffect, useState } from "react";
import NoteItem from "./components/NoteItem";
import axios from "axios";

function App() {
  const [data, setData] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [searchFields, setSearchFields] = useState(["name", "tags"]);

  useEffect(() => {
    if (searchQuery.trim() === "") {
      setData([]);
      return;
    }

    const fetchData = async () => {
      try {
        const fieldsQuery = searchFields.map((field) => `field=${field}`).join("&");
        const url = `http://127.0.0.1:8000/api/notes/?q=${searchQuery}&${fieldsQuery}`;

        const response = await axios.get(url);
        setData(response.data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, [searchQuery, searchFields]);

  return (
    <div className="container mt-5">
      {/* ช่องค้นหา */}
      <div className="row justify-content-center">
        <div className="col-md-8">
          <input
            type="text"
            className="form-control shadow-sm p-3 mb-4 rounded"
            placeholder="ค้นหาโน้ต..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
        </div>
      </div>

      {/* ตัวเลือกฟิลด์ค้นหา */}
      <div className="row justify-content-center">
        <div className="col-md-8 d-flex gap-3 mb-4">
          <div className="form-check">
            <input
              className="form-check-input"
              type="checkbox"
              checked={searchFields.includes("name")}
              onChange={() =>
                setSearchFields((prev) =>
                  prev.includes("name") ? prev.filter((f) => f !== "name") : [...prev, "name"]
                )
              }
            />
            <label className="form-check-label">ค้นหาจากชื่อ</label>
          </div>

          <div className="form-check">
            <input
              className="form-check-input"
              type="checkbox"
              checked={searchFields.includes("tags")}
              onChange={() =>
                setSearchFields((prev) =>
                  prev.includes("tags") ? prev.filter((f) => f !== "tags") : [...prev, "tags"]
                )
              }
            />
            <label className="form-check-label">ค้นหาจากแท็ก</label>
          </div>
        </div>
      </div>

      {/* แสดงรายการโน้ตที่ค้นพบ */}
      <div className="row justify-content-center">
        <div className="col-md-8">
          {data.length > 0 ? (
            <div className="list-group shadow-sm">
              {data.map((note) => (
                <NoteItem key={note.id} id={`note-${note.id}`} note={note} className="list-group-item" />
              ))}
            </div>
          ) : (
            <p className="text-center text-muted">กรุณาป้อนข้อความเพื่อค้นหา</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;