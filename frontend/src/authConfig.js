export const msalConfig = {
  auth: {
    clientId: "167adf65-9d11-4d67-8433-c33ca0d5ba0c",  // Your frontend app client ID from Azure AD
    authority: "https://login.microsoftonline.com/0d7f219a-ad11-4fbf-b91b-8d223731a2a7", // Your Azure AD Tenant ID
    redirectUri: "http://localhost:3000/manage",  // Ensure this is registered in Azure Portal
  },
  cache: {
    cacheLocation: "sessionStorage",  // Options: "localStorage" or "sessionStorage"
    storeAuthStateInCookie: false,    // Set to true if issues occur with some browsers
  },
};

// Request object to acquire access tokens for protected resources
export const loginRequest = {
  scopes: [
    "openid",  // Grants access to basic profile information
    "profile", // Access user's profile
    "api://c0b855d9-d4ce-4d41-a3e3-b998b4113ca6/access_as_user", // Access the backend API
  ],
};
