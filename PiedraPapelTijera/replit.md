# Rock Paper Scissors Game

## Overview

This is a simple Rock Paper Scissors game built with Streamlit, a Python web framework for creating interactive web applications. The game allows users to play against a computer opponent that makes random choices. The application tracks scores across multiple rounds and displays game results in real-time through a web interface.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: Streamlit - chosen for its simplicity in creating interactive web applications with minimal code
- **UI Components**: Uses Streamlit's built-in widgets and components for user interaction
- **State Management**: Leverages Streamlit's session state to persist game data across user interactions

### Game Logic Architecture
- **Core Game Engine**: Pure Python functions handle game mechanics
- **Winner Determination**: Uses conditional logic to implement Rock Paper Scissors rules
- **Random Choice Generation**: Computer opponent uses Python's random module for fair gameplay
- **Score Tracking**: Persistent scoring system that maintains player vs computer statistics

### Data Management
- **Session State**: All game data (scores, game history, last moves) stored in Streamlit's session state
- **No Persistent Storage**: Game data is temporary and resets when the session ends
- **State Initialization**: Centralized function ensures all required state variables are properly initialized

### Application Structure
- **Single File Architecture**: Entire application contained in one Python file for simplicity
- **Function-Based Design**: Modular functions for initialization, game logic, and winner determination
- **Event-Driven Interactions**: User actions trigger game rounds through Streamlit's reactive model

## External Dependencies

### Core Dependencies
- **Streamlit**: Web framework for creating the user interface and handling user interactions
- **Python Standard Library**: 
  - `random` module for computer choice generation
  - No additional external packages required

### Runtime Environment
- **Python**: Requires Python 3.6+ for Streamlit compatibility
- **Web Browser**: Any modern web browser for accessing the Streamlit interface
- **Local Development**: Runs locally via Streamlit's development server

The application is designed to be lightweight and self-contained, with minimal external dependencies to ensure easy setup and deployment.