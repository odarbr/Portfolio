import React from 'react';

const QuizQuestion = ({ question, onAnswer }) => (
    <div className="my-2">
        <p>{question}</p>
        <button onClick={() => onAnswer('yes')} className="mr-2">Yes</button>
        <button onClick={() => onAnswer('no')}>No</button>
    </div>
);

export default QuizQuestion;

