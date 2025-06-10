import React from 'react';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import QuizPage from './pages/QuizPage.jsx';

const App = () => (
    <Router>
        <Routes>
            <Route path="/" element={<QuizPage />} />
        </Routes>
    </Router>
);

export default App;