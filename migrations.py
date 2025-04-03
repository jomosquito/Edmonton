#This migration code is to update the database schema
#Made by Niket Gupta

from main import db, app, MedicalWithdrawalRequest
import sqlalchemy as sa
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

with app.app_context():
    # Create all tables if they don't exist
    logger.info("Creating database tables...")
    db.create_all()

    # Now try to add admin_viewed column if table exists
    try:
        with db.engine.connect() as conn:
            inspector = sa.inspect(db.engine)

            # Check if medical_withdrawal_request table exists
            if 'medical_withdrawal_request' in inspector.get_table_names():
                logger.info("Found medical_withdrawal_request table, checking columns...")

                # Check if admin_viewed column exists
                columns = inspector.get_columns('medical_withdrawal_request')
                if 'admin_viewed' not in [col['name'] for col in columns]:
                    logger.info("Adding admin_viewed column...")
                    conn.execute(sa.text('ALTER TABLE medical_withdrawal_request ADD COLUMN admin_viewed TEXT'))
                    logger.info("admin_viewed column added successfully.")
                else:
                    logger.info("admin_viewed column already exists.")
            else:
                logger.info("medical_withdrawal_request table doesn't exist yet, will be created with db.create_all()")

        db.session.commit()
        logger.info("Database migration completed successfully.")

    except Exception as e:
        logger.error(f"Error during migration: {str(e)}")
        db.session.rollback()
        # Continue execution even if migration fails
        logger.info("Migration error, but continuing with application startup...")