// src/app/api/sor+api.ts
import { GoogleGenAI } from '@google/genai';
import { SKILL } from '../../ai/skill';
import veri from '../../data/veri.json';

const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

export async function POST(request: Request) {
  const { soru } = await request.json();
  if (!soru || soru.length > 2000) {
    return Response.json({ hata: 'Geçersiz soru' }, { status: 400 });
  }

  try {
    const interaction = await ai.interactions.create({
      model: 'gemini-3.8-flash',
      input: `${SKILL}\n\nUygulamanın verisi:\n${JSON.stringify(veri)}\n\nKullanıcı sorusu: ${soru}`,
    });
    return Response.json({ cevap: interaction.output_text });
  } catch (e) {
    return Response.json(
      { hata: 'AI şu an yanıt veremiyor; biraz sonra tekrar deneyin.' },
      { status: 503 }
    );
  }
}
