# npc.py
import os
from groq import Groq
from dotenv import load_dotenv

# 🚨 AVISO DE SEGURANÇA: Nunca deixe sua chave exposta se for enviar para o GitHub!
# O ideal é usar variáveis de ambiente, mas para testarmos localmente agora,
# você pode colar sua chave diretamente aqui se preferir.
load_dotenv()


class NpcAI:
    @staticmethod
    def conversar_com_campones(player_name: str):
        """Gerencia a conversa por IA com o Camponês antes do Goblin."""
        api_key = os.environ.get("GROQ_API_KEY")

        if not api_key:
            print("\n❌  Erro: Chave GROQ_API_KEY não encontrada!")
            print("Crie um arquivo .env na raiz do projeto e adicione sua chave lá.")
            return

        try:
            client = Groq(api_key=api_key)
        except Exception:
            print(
                "\n❌ Erro ao inicializar a Groq. Verifique sua API Key no arquivo npc.py!"
            )
            return

        # Contexto (System Prompt) para moldar a personalidade do NPC
        contexto_npc = (
            "Você é um camponês humilde e desesperado em um jogo de RPG de texto. "
            "Um Goblin Saqueador terrível está destruindo suas plantações de batata. "
            f"Um jovem herói chamado {player_name} acabou de chegar para falar com você. "
            "Seja imersivo, medieval, fale com medo do monstro, mas seja breve nas respostas (máximo 3 frases). "
            "Diga a ele que se ele quiser encerrar a conversa e partir para a luta, basta digitar 'sair'."
        )

        # Histórico da conversa para a IA lembrar do que foi dito
        historico = [{"role": "system", "content": contexto_npc}]

        print("\n" + "=" * 20 + " 🌾 INTERAÇÃO NARRATIVA " + "=" * 20)
        print(
            '[👨‍🌾NPC Camponês]: "Oh, graças aos céus! Um viajante! Por favor, me ouça..."'
        )
        print(
            "(Você pode conversar livremente com o Camponês. Digite 'sair' para encerrar o diálogo.)"
        )
        print("=" * 64)

        turnos_restantes = 4  # Limite de turnos de conversa que você sugeriu!

        while turnos_restantes > 0:
            print(f"\n💬 [Turnos de conversa restantes: {turnos_restantes}]")
            fala_jogador = input(f"[{player_name}]: ").strip()

            if fala_jogador.lower() == "sair":
                print(
                    '\n[👨‍🌾NPC Camponês]: "Entendo... O tempo está acabando para as minhas batatas!"'
                )
                break

            # Adiciona a fala do jogador ao histórico
            historico.append({"role": "user", "content": fala_jogador})

            print("\n🤖 [👨‍🌾Camponês pensando...] ")

            try:
                # Chamada oficial para o modelo Llama 3 70B via Groq
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=historico,
                    temperature=0.7,
                    max_tokens=150,
                )

                resposta_npc = completion.choices[0].message.content
                print(f'\n[👨‍🌾NPC Camponês]: "{resposta_npc}"')

                # Adiciona a resposta do NPC ao histórico para manter o contexto
                historico.append({"role": "assistant", "content": resposta_npc})

            except Exception as e:
                print(f"\n❌ Houve um erro na comunicação com a IA: {e}")
                print(
                    '[NPC Camponês]: "*O camponês chora confuso e aponta para o horizonte onde o Goblin está*"'
                )
                break

            turnos_restantes -= 1

        if turnos_restantes == 0:
            print(
                '\n[NPC Camponês]: "Não temos mais tempo para conversa! O monstro está se aproximando!"'
            )

        print("\n" + "=" * 64 + "\n")
