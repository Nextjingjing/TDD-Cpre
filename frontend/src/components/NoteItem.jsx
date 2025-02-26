import React from "react";

const NoteItem = ({ note }) => {
  return (
    <li className="note-item">
      <img
        src={note.thumbnail_url}
        alt={note.name}
        style={{ width: "120px", height: "auto", borderRadius: "8px" }}
      />
      <h3>{note.name}</h3>
      <p>Tags: {note.tags}</p>
      <p>Created At: {new Date(note.created_at).toLocaleString()}</p>
      <a href={note.file_url} target="_blank" rel="noopener noreferrer">
        Open File
      </a>
    </li>
  );
};

export default NoteItem;
