import React, { useState, useEffect } from 'react';
import axios from 'axios';

function UserProfile({ match }) {
    const [user, setUser] = useState({});

    useEffect(() => {
        axios.get(`/api/users/${match.params.id}/`)
            .then(response => {
                setUser(response.data);
            });
    }, [match.params.id]);

    return (
        <div className="container">
            <h2>{user.username}</h2>
            <p>{user.bio}</p>
            <p>Email: {user.email}</p>
        </div>
    );
}

export default UserProfile;
