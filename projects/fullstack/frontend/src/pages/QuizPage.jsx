import React, { useEffect, useState } from "react";
import QuizQuestion from "../components/QuizQuestion";
import ResultCard from "../components/ResultCard";

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

    const handleAnswer = (id, value) => {
        setAnswers(prev => ({ ...prev, [id]: value}));
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
        return <ResultCard result={result} />;
    }

    return (
        <div className="p-4">
            {questions.map(q => (
                <QuizQuestion
                    key={q.id}
                    question={q.question}
                    onAnswer={value => handleAnswer(q.id, value)}
                />
            ))}
            {questions.length > 0 && (
                <button onClick={handleSubmit} className="mt-4">Submit</button>
            )}
        </div>
    );
 };

 export default QuizPage;