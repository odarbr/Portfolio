import { Router } from 'express';

const router = Router();

router.post('/', (req, res) => {
    const { answers } = req.body;
    const yesCount = Object.values(answers || {}).filter(v => v === 'yes').length;
    const personality = yesCount > 1 ? 'Extrovert' : 'Introvert';
    res.json({ personality });
});

export default router;