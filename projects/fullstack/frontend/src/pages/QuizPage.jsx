import React, { useEffect, useState } from "react";

const QuizPage = () => {
    const [questions, setQuestions] = useState([]);
    const [answers, setAnswers] = useState({});
    const [submitted, setSubmitted] = useState(false);
    const [result, setResult] = useState(null);

    useEffect(() => {
        // Fetch questions from backend
        fetch("http://localhost:3001/quiz")
            .then(res => res.json())
            .then(setQuestions);
    }, []);

    const handleAnswer = (questionId, value) => {
        setAnswers(prev => ({ ...prev, [questionId]: value}));
    };

    const handleSubmit = async () => {
        const res = await fetch("http://localhost:3001/submit", {
            method: "POST",
            headers: { "Content-Type": "application/json"},
            body: JSON.stringify({ answers }),
        });

        const data = await res.json();
        setResult(data.personality);
        setSubmitted(true);
    };

    if (submitted) {
        return (
            <div className="p-4 text-center">
                <h2 className="text-2xl font-bold">Your Personality Type:</h2>
                <p className="text-xl mt-2">{result}</p>
            </div>
        );
    }

 }