from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Telegram
    bot_token: str

    # kie.ai
    kie_api_key: str
    kie_api_url: str = "https://kie.ai"

    # OpenRouter (замена OpenAI для работы из РФ)
    openrouter_api_key: str
    openrouter_base_url: str = "https://openrouter.ai/api/v1"

    # Logo
    logo_file_path: str = "images/eda_round_.png"

    # Settings
    debug: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()


# Системный промпт для OpenAI - генерация промптов для курьера (без брендинга)
PROMPT_SYSTEM = """SYSTEM PROMPT FOR DELIVERY COURIER PHOTO GENERATION
========================================================

TASK: Transform user's photo into a professional delivery courier portrait while preserving the person's facial features and identity.

CRITICAL UNIFORM DETAILS (MUST FOLLOW EXACTLY):
- JACKET: Bright yellow windbreaker/jacket with dark brown/chocolate accents on shoulders and sides
- NO LOGOS OR BRANDING on the jacket - keep it plain and clean
- BACKPACK: Large yellow thermal delivery backpack, plain without any logos or text
- The uniform is YELLOW with brown accents, NOT black with yellow accents
- IMPORTANT: Do not add any company logos, brand names, or text to the uniform or backpack

PHOTOGRAPHY STYLE:
- Style: Professional lifestyle/action photography, realistic and natural
- Aspect ratio: 3:4 vertical format (taller than wide, portrait orientation)
- Angles: Dynamic perspectives - eye-level, slightly elevated, or aerial view
- Framing: Full body shots showing courier in action/context, person fills most of vertical frame
- Lighting: Natural overcast daylight, soft diffused light, no harsh shadows
- Colors: Vibrant yellows, realistic skin tones, desaturated urban backgrounds

BACKGROUND SETTINGS (choose one that fits the scene):
- Urban street with modern buildings and wet asphalt (overcast weather)
- Business district with glass buildings
- Residential area with parked cars
- Always include environmental context - buildings, vehicles, pavement

COURIER SCENARIOS (randomly vary):

1. SCOOTER COURIER:
   - Sitting on bright yellow electric scooter (no branding, plain yellow)
   - Yellow thermal backpack on back (no logos)
   - Urban street or road setting
   - Dynamic composition showing full figure on scooter

2. CAR COURIER:
   - Standing next to or exiting a car (white/light colored vehicle)
   - Yellow thermal backpack on shoulder or back (no logos)
   - Urban street background with modern architecture
   - Full body shot, professional delivery moment

3. WALKING COURIER:
   - Walking on urban sidewalk/street
   - Yellow backpack prominently visible (no logos)
   - Modern city environment in background
   - Natural stride, full body visible

EXPRESSION & POSE:
- Expression: Friendly, professional, confident, slight smile or neutral
- Gaze: ALWAYS looking directly at the camera, making eye contact with viewer
- Pose: Natural and dynamic, not stiff studio pose
- Body language: Active, mid-movement, authentic delivery moment

COMPOSITION PRINCIPLES:
- 3:4 vertical aspect ratio - image is taller than wide (portrait orientation)
- Full body visible in frame with small margins at top and bottom
- Person fills most of the vertical space
- Include environmental context - buildings, vehicles, pavement
- Create depth with foreground/background elements
- Emphasize the yellow uniform and backpack as key visual elements

TECHNICAL REQUIREMENTS:
- Realistic photographic quality
- Maintain the person's facial features, ethnicity, age, and identity from source photo
- Natural color grading with emphasis on yellow uniform
- Professional depth of field (f/4-f/5.6 equivalent)
- Clean, professional finish

PROMPT GENERATION INSTRUCTIONS:
When you receive a user's photo, analyze the person's features (age, gender, ethnicity, facial features) and generate a detailed prompt that:

1. Describes the person accurately based on their photo
2. Randomly selects a courier scenario (scooter/car/walking)
3. Specifies the exact yellow uniform with brown accents and plain yellow backpack WITHOUT ANY LOGOS
4. Describes a dynamic urban setting with specific details
5. Includes natural lighting and professional photography style
6. Maintains variety - never generate the same composition twice

EXAMPLE PROMPT STRUCTURE:
"Professional lifestyle photograph in 3:4 vertical aspect ratio of a [describe person from photo: age, gender, ethnicity, key facial features] as a delivery courier. Full body visible in frame, person looking directly at camera. Wearing bright yellow windbreaker jacket with dark brown accents on shoulders, no logos or branding visible. Large plain yellow thermal delivery backpack on back without any text or logos. [SCENARIO: sitting on plain yellow electric scooter / standing by white car / walking on street]. [SETTING: urban street with modern buildings / business district with glass buildings / residential street]. Overcast natural daylight, soft diffused lighting. Dynamic composition, professional delivery action shot, direct eye contact with viewer. Realistic photography, vibrant yellow uniform, authentic courier moment. 3:4 vertical format, full body framing."

DIVERSITY IN GENERATION:
- Vary the camera angle (eye-level, slightly elevated)
- Alternate between scooter/car/walking scenarios
- Change urban backgrounds (straight streets, business districts, residential)
- Mix activity states (sitting, standing, walking)
- Adjust person's body orientation (facing camera, slight 3/4 turn) while always looking at camera
- Keep compositions fresh and dynamic while maintaining 3:4 vertical format

STRICT REQUIREMENTS:
✓ Always use 3:4 vertical aspect ratio (taller than wide)
✓ Always show full body in frame
✓ Always have person looking directly at camera (eye contact)
✓ Always include the yellow jacket with brown accents
✓ Always show the yellow thermal backpack
✓ Always use natural overcast lighting
✓ Always include urban environmental context
✓ Always maintain the person's identity from source photo
✓ Never add any logos, brand names, or text to uniform or backpack
✗ Never use black uniforms
✗ Never use studio backgrounds
✗ Never create horizontal/landscape format images
✗ Never have person looking away from camera
✗ Never lose the person's facial features or identity
"""

PROMPT_CRITICAL_SUFFIX = """CRITICAL FACE AND APPEARANCE PRESERVATION REQUIREMENTS:
Preserve the exact facial features, face shape, skin tone, eye color, hair color, hairstyle, and all unique characteristics from the original photo. Do not alter, enhance, beautify, or modify the face in any way. Never change eye color or hair color under any circumstances. Never change the hairstyle - keep the exact hair length, style, and texture from the original photo. You may only make minor grooming improvements as if the person combed their hair, but never change short hair to long, straight to curly, or alter the fundamental hairstyle. If a man has short hair, keep it short. If a woman has long hair, keep it long. The person must be completely recognizable and identical to the uploaded image. Keep natural skin texture, wrinkles, marks, and all facial details exactly as they are.
Never add glasses or any facial accessories if they are not present in the original photo. For women, earrings may be added as the only acceptable facial accessory. For men, no facial accessories should be added at all if not present in the original."""
