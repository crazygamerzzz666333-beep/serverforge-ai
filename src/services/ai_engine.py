"""AI engine for natural language processing."""
import re
from typing import Dict, List, Any
from src.logging import get_logger

logger = get_logger(__name__)


class AIEngine:
    """AI engine for server management commands."""

    def __init__(self):
        """Initialize AI engine."""
        self.themes = {
            "minecraft": {
                "color": 0x2ECC71,
                "style": "blocky",
                "channels": ["📋-rules", "💬-general", "🎮-gaming"]
            },
            "gaming": {
                "color": 0x9B59B6,
                "style": "modern",
                "channels": ["#announcements", "#gaming", "#streaming"]
            },
            "professional": {
                "color": 0x3498DB,
                "style": "corporate",
                "channels": ["#general", "#announcements", "#support"]
            },
            "minimal": {
                "color": 0x95A5A6,
                "style": "clean",
                "channels": ["#general", "#support"]
            },
            "dark": {
                "color": 0x2C3E50,
                "style": "dark",
                "channels": ["#general", "#off-topic", "#support"]
            }
        }

    def parse_command(self, text: str) -> Dict[str, Any]:
        """Parse natural language command."""
        text_lower = text.lower()
        
        commands = {
            "improve": r"improve|suggest|optimize",
            "theme": r"theme|style|look",
            "channel": r"channel|create",
            "role": r"role|permission",
        }
        
        for cmd, pattern in commands.items():
            if re.search(pattern, text_lower):
                return {"type": cmd, "text": text}
        
        return {"type": "unknown", "text": text}

    def suggest_improvements(self, guild_data: Dict) -> List[str]:
        """Get server improvement suggestions."""
        suggestions = []
        
        if guild_data.get("channels_count", 0) < 5:
            suggestions.append("🏗️ Add more organized categories")
        
        if guild_data.get("roles_count", 0) < 3:
            suggestions.append("👥 Create more roles for hierarchy")
        
        if guild_data.get("member_count", 0) > 100 and guild_data.get("roles_count", 0) < 5:
            suggestions.append("🛡️ Add more moderator roles")
        
        suggestions.append("📊 Enable analytics for tracking")
        suggestions.append("🤖 Use AI to improve server layout")
        
        return suggestions[:5]

    def get_theme(self, theme_name: str) -> Dict[str, Any]:
        """Get theme configuration."""
        return self.themes.get(theme_name.lower(), self.themes["professional"])


ai_engine = AIEngine()
