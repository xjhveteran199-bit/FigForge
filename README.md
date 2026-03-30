# FigForge v1.0

**Precision Prompt Engine for Scientific Illustration**

FigForge is a web-based tool that generates optimized prompts for Nano Banana 2 (Google Gemini's image generation model), specifically designed for high-accuracy scientific figures.

## Features

### Generate Mode — Harness Engineering Framework
- **7-step guided wizard** to build precise scientific illustration prompts
- **9 journal presets** with real specs from Nature, Science, Cell, ACS, Wiley, RSC, Elsevier, PNAS
- **Dual-Lock Precision**: positive constraints + negative constraints for scientific accuracy
- Bilingual output (English / Chinese)

### Refine Mode — Visual Refine Engine
- **Upload & box-select** regions on existing AI-generated figures
- **Spatial Translation Engine**: converts pixel coordinates to AI-friendly natural language
- **7 edit types**: Remove, Move, Replace, Recolor, Label, Resize, Modify
- **Multi-edit queue** with batch prompt generation

## Usage

1. Open `nanobanana2-prompt-generator.html` in any modern browser
2. **Generate**: Follow the 7-step wizard to create a prompt from scratch
3. **Refine**: Upload an AI figure, draw boxes on areas to edit, generate edit prompts
4. Copy the prompt → paste into Google Gemini (Nano Banana 2) → get your figure

## Tech

Single HTML file. No dependencies. No build step. No server required.

## License

MIT
