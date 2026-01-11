import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [user, setUser] = useState(null);

  const ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY4MTU4NTk2LCJpYXQiOjE3NjgxNTQ5OTYsImp0aSI6ImM2M2EyNTE1ZThiNjRkMzNhYzM3ZGFkNDczNWNmNDczIiwidXNlcl9pZCI6IjQifQ.RRoACe2SKd8s2I-y_X0bOkXHp-w5Byxy1wtFsZODd5A";

  useEffect(() => {
    fetch("http://127.0.0.1:8000/accounts/me/", {
      headers: {
        Authorization: `Bearer ${ACCESS_TOKEN}`,
      },
    })
      .then((res) => res.json())
      .then((data) => setUser(data));
  }, []);

  return (
    <div className="container">
      <h1>JWT Test</h1>

      {user ? (
        <p>
          Logged in as: <strong>{user.username}</strong> | Staff:{" "}
          <strong>{user.is_staff ? "Yes" : "No"}</strong>
        </p>
      ) : (
        <p>Loading user...</p>
      )}
    </div>
  );
}

export default App;
