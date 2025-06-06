# Price Comparison - Find Lower Prices Instantly

Save Time and Money — Instantly Compare Prices and Find Better Deals from Other Sites as you Browse!

## Setup

### Prerequisites

- Python (version 3.8 or higher)
- pip (Python package installer)

### Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd pricecomparison-api
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root:
   ```
   API_BASE_URL=
   ```

### Development

1. Start the development server:
   ```bash
   python3 -m uvicorn main:app --reload
   ```

2. The API will be available at `http://localhost:8000`

3. The Swagger docs will be available at `http://localhost:8000/docs`