import React from 'react';
import '../Home/Admin.css'; // Import the CSS file

const Profile = () => {
  return (
    <div className="profile-container">
      <div className="profile-header">
        <img 
          src="https://thumbs.dreamstime.com/b/businessman-icon-vector-male-avatar-profile-image-profile-businessman-icon-vector-male-avatar-profile-image-182095609.jpg" 
          alt="Profile" 
          className="profile-picture" 
        />
        <h1 className="profile-name">ADMPR</h1>
      </div>
      <div className="profile-body">
        <p className="profile-bio">
          ADMIN
        </p>
        <div className="profile-contact">
          <h3>Contact Information</h3>
          <p>Email: xyz@example.com</p>
          <p>Phone: 123 456 7890</p>
        </div>
        <button className="profile-button">Show Table</button>
      </div>
    </div>
  );
};

export default Profile;