# Current Architecture

User
 ↓
Input Career
 ↓
State
 ↓
Skill Generator
 ↓
State Update
 ↓
Roadmap Generator
 ↓
State Update
 ↓
Salary Generator
 ↓
Final State

# Enterprise Considerations

1. State should be small
2. Avoid storing unnecessary data
3. State must be serializable
4. State updates should be predictable

# Future Improvements

1. LangGraph StateGraph
2. Persistent Storage
3. Checkpointing
4. Memory Management