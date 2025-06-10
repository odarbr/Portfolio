import React from 'react';
import { useLocation } from 'react-router-dom';
import ResultCard from '../components/ResultCard';

const ResultPage = () => {
    const { state } = useLocation();
    const result = state?.result;

    if (!result) {
        return <p>No result available.</p>;
    }

    return <ResultCard result={result} />;
};

export default ResultPage;