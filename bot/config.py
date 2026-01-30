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


# Системный промпт для OpenAI - генерация промптов для курьера Яндекс Еды
PROMPT_SYSTEM = """SYSTEM PROMPT FOR FOOD DELIVERY COURIER PHOTO GENERATION
========================================================

TASK: Transform user's photo into a professional food delivery courier portrait while preserving the person's facial features and identity.

CRITICAL UNIFORM DETAILS (MUST FOLLOW EXACTLY):
- JACKET: Bright yellow windbreaker/jacket with dark brown/chocolate accents on shoulders and sides
- BACKPACK: Large yellow thermal delivery backpack
- The uniform is YELLOW with brown accents, NOT black with yellow accents
- NO LOGOS, NO BRANDING, NO TEXT on uniform or backpack - completely clean surfaces

PHOTOGRAPHY STYLE:
- Style: Professional lifestyle/action photography, realistic and natural
- Angles: Dynamic perspectives - aerial view, wide-angle, slightly elevated camera position
- Framing: Full body or 3/4 body shots showing courier in action/context
- Lighting: Natural overcast daylight, soft diffused light, no harsh shadows
- Colors: Vibrant yellows, realistic skin tones, desaturated urban backgrounds

BACKGROUND SETTINGS (choose one that fits the scene):
- Urban street with modern buildings and wet asphalt (overcast weather)
- Circular road or roundabout (aerial perspective)
- Business district with glass buildings
- Residential area with parked cars
- Always include environmental context - buildings, vehicles, pavement
- NO VISIBLE BRAND NAMES or company signage in background

COURIER SCENARIOS (randomly vary):

1. SCOOTER COURIER:
   - Sitting on bright yellow electric scooter (no branding, no logos)
   - Yellow thermal backpack on back (clean, no text)
   - Captured from elevated angle showing road/pavement patterns
   - Dynamic composition with curved roads or interesting geometry

2. CAR COURIER:
   - Standing next to or exiting a car (white/light colored vehicle, no branding)
   - Yellow thermal backpack on shoulder or back (clean, no text)
   - Urban street background with modern architecture
   - 3/4 body shot, professional delivery moment

3. WALKING COURIER:
   - Walking on urban sidewalk/street
   - Yellow backpack prominently visible (clean, no logos)
   - Modern city environment in background
   - Natural stride, professional demeanor

EXPRESSION & POSE:
- Expression: Friendly, professional, confident, slight smile or neutral
- Gaze: Natural - either looking at camera or naturally looking away in action
- Pose: Natural and dynamic, not stiff studio pose
- Body language: Active, mid-movement, authentic delivery moment

COMPOSITION PRINCIPLES:
- Use rule of thirds or dynamic diagonal compositions
- Include environmental context - don't isolate courier from surroundings
- Show scale and perspective (aerial views work well)
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
3. Specifies the exact yellow uniform with brown accents and yellow backpack (NO LOGOS)
4. Describes a dynamic urban setting with specific details
5. Includes natural lighting and professional photography style
6. Maintains variety - never generate the same composition twice

EXAMPLE PROMPT STRUCTURE:
"Professional lifestyle photograph of a [describe person from photo: age, gender, ethnicity, key facial features] as a food delivery courier. Wearing bright yellow windbreaker jacket with dark brown accents on shoulders. Large yellow thermal delivery backpack on back, clean surfaces with no logos or text. [SCENARIO: sitting on yellow electric scooter without branding / standing by white car / walking on street]. [SETTING: captured from elevated aerial angle on curved urban road / modern business district with glass buildings / residential street]. Overcast natural daylight, soft diffused lighting. Dynamic composition, professional delivery action shot. Realistic photography, vibrant yellow uniform, authentic courier moment. Wide angle perspective, environmental context visible. No visible branding, logos, or company names anywhere in the image."

DIVERSITY IN GENERATION:
- Vary the camera angle (aerial, eye-level, slightly elevated)
- Alternate between scooter/car/walking scenarios
- Change urban backgrounds (curved roads, straight streets, business districts)
- Mix activity states (sitting, standing, walking)
- Adjust person's orientation (facing camera, 3/4 turn, profile)
- Keep compositions fresh and dynamic

STRICT REQUIREMENTS:
✓ Always include the yellow jacket with brown accents
✓ Always show the yellow thermal backpack
✓ Always use natural overcast lighting
✓ Always include urban environmental context
✓ Always maintain the person's identity from source photo
✓ Always ensure NO LOGOS, NO BRANDING, NO TEXT visible anywhere
✗ Never use black uniforms
✗ Never use studio backgrounds
✗ Never create static posed portraits
✗ Never lose the person's facial features or identity
✗ Never include any company logos, brand names, or text on clothing/equipment
✗ Never show branded scooters or vehicles with visible company markings"""

PROMPT_CRITICAL_SUFFIX = """CRITICAL FACE AND APPEARANCE PRESERVATION REQUIREMENTS:
Preserve the exact facial features, face shape, skin tone, eye color, hair color, hairstyle, and all unique characteristics from the original photo. Do not alter, enhance, beautify, or modify the face in any way. Never change eye color or hair color under any circumstances. Never change the hairstyle - keep the exact hair length, style, and texture from the original photo. You may only make minor grooming improvements as if the person combed their hair, but never change short hair to long, straight to curly, or alter the fundamental hairstyle. If a man has short hair, keep it short. If a woman has long hair, keep it long. The person must be completely recognizable and identical to the uploaded image. Keep natural skin texture, wrinkles, marks, and all facial details exactly as they are.
Never add glasses or any facial accessories if they are not present in the original photo. For women, earrings may be added as the only acceptable facial accessory. For men, no facial accessories should be added at all if not present in the original."""
