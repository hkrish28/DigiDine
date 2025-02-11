// App.js - Entry point
import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import SignUp from './SignUp';
import SignUpChef from './SignUpChef';
import SignUpOption from './SignUpOption';
import Home from './Home';
import Header from './Header';
import CssBaseline from '@mui/material/CssBaseline';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import ProfilePage from './ProfilePage';

const defaultTheme = createTheme();


const App = () => {
  const [loggedIn, setLoggedIn] = useState(sessionStorage.getItem('loggedIn') === 'true');
  
  return (
    <Router>
        <ThemeProvider theme={defaultTheme}>
      <CssBaseline />
      <Header loggedIn={loggedIn} setLoggedIn={setLoggedIn} />
      <Routes>
        <Route path="/" element={<Home loggedIn={loggedIn} setLoggedIn={setLoggedIn} />} />
        <Route path="/signup"  element={<SignUp />} />
        <Route path="/signupOption"  element={<SignUpOption />} />
        <Route path="/signupchef"  element={<SignUpChef />} />
        <Route path="/profile"  element={<ProfilePage setLoggedIn={setLoggedIn} />} />
      </Routes>
      </ThemeProvider>
    </Router>
  );
};

export default App;
