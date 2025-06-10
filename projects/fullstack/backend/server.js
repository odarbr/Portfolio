import express from 'express';
import cors from 'cors';

import quizRoutes from './routes/quizRoutes.js';
import resultRoutes from './routes/resultRoutes.js';

const app = express();
app.use(cors());
app.use(express.json());

app.use('/quiz', quizRoutes);
app.use('/submit', resultRoutes);

app.listen(3001, () => console.log('Server running on http://localhost:3001'));
