import { Router } from 'express';

const router = Router();

const questions = [
    { id: 1, question: 'Do you dislike social gatherings?' },
    { id: 2, question: 'Do you have stage fear?' },
    { id: 3, question: 'Do you get drained from socializing?' }
];

router.get('/', (req, res) => {
    res.json(questions);
});

export default router;