import React from 'react';

const ResultCard = ({ result }) => (
    <div className="p-4 text-center">
        <h2 className="text-2xl font-bold">Your personality type:</h2>
        <p className="text-xl mt-2">{result}</p>
    </div>
);

export default ResultCard;
