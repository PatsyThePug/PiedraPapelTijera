import streamlit as st
import random

def initialize_session_state():
    """Initialize session state variables for the game"""
    if 'participants' not in st.session_state:
        # Pre-register 2 participants as requested
        st.session_state.participants = {
            'Jugador1': {
                'wins': 0,
                'losses': 0,
                'ties': 0,
                'total_games': 0
            },
            'Jugador2': {
                'wins': 0,
                'losses': 0,
                'ties': 0,
                'total_games': 0
            }
        }
    if 'current_participant' not in st.session_state:
        # Set first participant as current
        participant_names = list(st.session_state.participants.keys())
        st.session_state.current_participant = participant_names[0] if participant_names else None
    if 'last_result' not in st.session_state:
        st.session_state.last_result = None
    if 'last_player_choice' not in st.session_state:
        st.session_state.last_player_choice = None
    if 'last_computer_choice' not in st.session_state:
        st.session_state.last_computer_choice = None

def determine_winner(player_choice, computer_choice):
    """Determine the winner using conditional logic"""
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "player"
    else:
        return "computer"

def register_participant(name):
    """Register a new participant"""
    if name and name not in st.session_state.participants:
        st.session_state.participants[name] = {
            'wins': 0,
            'losses': 0,
            'ties': 0,
            'total_games': 0
        }
        st.session_state.current_participant = name
        return True
    return False

def get_current_participant_data():
    """Get current participant's data"""
    if st.session_state.current_participant:
        return st.session_state.participants[st.session_state.current_participant]
    return None

def play_game(player_choice):
    """Main game logic"""
    if not st.session_state.current_participant:
        st.error("Por favor registra un participante primero")
        return
    
    # Computer makes random choice
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    # Determine winner
    result = determine_winner(player_choice, computer_choice)
    
    # Update game state
    st.session_state.last_player_choice = player_choice
    st.session_state.last_computer_choice = computer_choice
    
    # Update participant scores
    participant_data = st.session_state.participants[st.session_state.current_participant]
    participant_data['total_games'] += 1
    
    if result == "player":
        participant_data['wins'] += 1
        st.session_state.last_result = f"{st.session_state.current_participant} Gana! 🎉"
    elif result == "computer":
        participant_data['losses'] += 1
        st.session_state.last_result = "Computadora Gana! 🤖"
    else:
        participant_data['ties'] += 1
        st.session_state.last_result = "¡Empate! 🤝"

def reset_participant_data():
    """Reset current participant's statistics"""
    if st.session_state.current_participant:
        participant_data = st.session_state.participants[st.session_state.current_participant]
        participant_data['wins'] = 0
        participant_data['losses'] = 0
        participant_data['ties'] = 0
        participant_data['total_games'] = 0
        st.session_state.last_result = None
        st.session_state.last_player_choice = None
        st.session_state.last_computer_choice = None

def reset_all_data():
    """Reset all participants and game data"""
    st.session_state.participants = {}
    st.session_state.current_participant = None
    st.session_state.last_result = None
    st.session_state.last_player_choice = None
    st.session_state.last_computer_choice = None

def get_choice_emoji(choice):
    """Return emoji representation of choice"""
    if choice == "Rock":
        return "🪨"
    elif choice == "Paper":
        return "📄"
    elif choice == "Scissors":
        return "✂️"
    return ""

def main():
    """Main application function"""
    # Initialize session state
    initialize_session_state()
    
    # App title and description
    st.title("🎮 Rock Paper Scissors")
    st.markdown("¡Elige tu arma y desafía a la computadora!")
    
    # Participant registration section
    st.markdown("---")
    st.markdown("### 📝 Registro de Participantes")
    
    reg_col1, reg_col2 = st.columns([2, 1])
    
    with reg_col1:
        new_participant = st.text_input("Nombre del participante:", placeholder="Ingresa tu nombre")
    
    with reg_col2:
        if st.button("✅ Registrar", width="stretch"):
            if new_participant:
                if register_participant(new_participant):
                    st.success(f"¡{new_participant} registrado!")
                    st.rerun()
                else:
                    st.warning("El participante ya existe o nombre inválido")
            else:
                st.warning("Por favor ingresa un nombre")
    
    # Participant selection
    if st.session_state.participants:
        st.markdown("### 👤 Seleccionar Participante")
        participant_names = list(st.session_state.participants.keys())
        
        # Create selectbox for choosing participant
        selected = st.selectbox(
            "Participante actual:",
            participant_names,
            index=participant_names.index(st.session_state.current_participant) if st.session_state.current_participant in participant_names else 0
        )
        
        if selected != st.session_state.current_participant:
            st.session_state.current_participant = selected
            st.rerun()
    
    # Only show game if participant is selected
    if st.session_state.current_participant:
        st.markdown("---")
        st.markdown(f"### 🎯 Jugando como: **{st.session_state.current_participant}**")
        
        # Game controls section
        st.markdown("### Haz tu elección")
        
        # Create three columns for game buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🪨 Piedra", width="stretch"):
                play_game("Rock")
        
        with col2:
            if st.button("📄 Papel", width="stretch"):
                play_game("Paper")
        
        with col3:
            if st.button("✂️ Tijeras", width="stretch"):
                play_game("Scissors")
        
        # Display last game result if available
        if st.session_state.last_result:
            st.markdown("---")
            st.markdown("### Resultado del Último Juego")
            
            # Show choices and result
            result_col1, result_col2, result_col3 = st.columns(3)
            
            with result_col1:
                st.markdown(f"**{st.session_state.current_participant}:** {get_choice_emoji(st.session_state.last_player_choice)} {st.session_state.last_player_choice}")
            
            with result_col2:
                st.markdown("**VS**")
            
            with result_col3:
                st.markdown(f"**Computadora:** {get_choice_emoji(st.session_state.last_computer_choice)} {st.session_state.last_computer_choice}")
            
            # Display result with appropriate styling
            if "Gana" in st.session_state.last_result and st.session_state.current_participant in st.session_state.last_result:
                st.success(st.session_state.last_result)
            elif "Computadora Gana" in st.session_state.last_result:
                st.error(st.session_state.last_result)
            else:
                st.info(st.session_state.last_result)
        
        # Score tracking section for current participant
        participant_data = get_current_participant_data()
        if participant_data and participant_data['total_games'] > 0:
            st.markdown("---")
            st.markdown(f"### 📊 Estadísticas de {st.session_state.current_participant}")
            
            # Display scores in columns
            score_col1, score_col2, score_col3, score_col4 = st.columns(4)
            
            with score_col1:
                st.metric("Victorias", participant_data['wins'])
            
            with score_col2:
                st.metric("Derrotas", participant_data['losses'])
            
            with score_col3:
                st.metric("Empates", participant_data['ties'])
            
            with score_col4:
                st.metric("Total Juegos", participant_data['total_games'])
            
            # Calculate and display win percentage
            if participant_data['total_games'] > 0:
                win_percentage = (participant_data['wins'] / participant_data['total_games']) * 100
                st.progress(win_percentage / 100)
                st.markdown(f"**Porcentaje de Victorias:** {win_percentage:.1f}%")
        
        # Reset buttons
        st.markdown("---")
        reset_col1, reset_col2 = st.columns(2)
        
        with reset_col1:
            if st.button("🔄 Reiniciar Participante", type="secondary"):
                reset_participant_data()
                st.rerun()
        
        with reset_col2:
            if st.button("🗑️ Borrar Todo", type="secondary"):
                reset_all_data()
                st.rerun()
    
    # Show all participants summary
    if st.session_state.participants:
        st.markdown("---")
        st.markdown("### 🏆 Tabla de Participantes")
        
        # Create a summary table
        participants_data = []
        for name, data in st.session_state.participants.items():
            if data['total_games'] > 0:
                win_rate = (data['wins'] / data['total_games']) * 100
                participants_data.append({
                    'Participante': name,
                    'Victorias': data['wins'],
                    'Derrotas': data['losses'],
                    'Empates': data['ties'],
                    'Total': data['total_games'],
                    'Win Rate %': f"{win_rate:.1f}%"
                })
        
        if participants_data:
            import pandas as pd
            df = pd.DataFrame(participants_data)
            st.dataframe(df, width=600)
    
    # Game rules section (collapsible)
    with st.expander("📋 Reglas del Juego"):
        st.markdown("""
        **Cómo Jugar:**
        - Piedra vence a Tijeras
        - Tijeras vence a Papel  
        - Papel vence a Piedra
        - La misma elección resulta en empate
        
        **Puntuación:**
        - Victoria: +1 punto para el participante
        - Derrota: +1 punto para la computadora
        - Empate: No se otorgan puntos
        """)

if __name__ == "__main__":
    main()
