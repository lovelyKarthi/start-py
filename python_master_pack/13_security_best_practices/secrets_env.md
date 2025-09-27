Secrets & env best practices:
- Do not commit .env to VCS
- Use dotenv for local dev, but use vault/secret manager in prod
- Example:
    from dotenv import load_dotenv
    load_dotenv()
    SECRET = os.getenv('SECRET')
