# create_large_sample_data.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def sample_datasets():
    """Create larger sample dataset files with 200 samples each"""
    
    # Create timestamp base - 200 samples with 1-second intervals
    base_time = datetime(2024, 1, 15, 10, 0, 0)
    timestamps = [base_time + timedelta(seconds=i) for i in range(200)]
    
    print("🔄 Creating large sample datasets (200 samples each)...")
    
    # 1. EEG Data - Brain wave patterns
    eeg_data = {
        'timestamp': timestamps,
        'alpha_power': [0.65 + 0.15 * np.sin(i/15) + 0.05 * np.cos(i/8) + np.random.normal(0, 0.02) for i in range(200)],
        'beta_power': [0.25 + 0.12 * np.cos(i/12) + 0.03 * np.sin(i/6) + np.random.normal(0, 0.015) for i in range(200)],
        'theta_power': [0.15 + 0.08 * np.sin(i/20) + 0.02 * np.cos(i/10) + np.random.normal(0, 0.01) for i in range(200)],
        'gamma_power': [0.08 + 0.04 * np.cos(i/25) + 0.01 * np.sin(i/15) + np.random.normal(0, 0.005) for i in range(200)]
    }
    pd.DataFrame(eeg_data).to_csv('sample_eeg_data.csv', index=False)
    print("✅ Created sample_eeg_data.csv with 200 samples")
    
    # 2. HRV Data - Heart Rate Variability
    hrv_data = {
        'timestamp': timestamps,
        'hr_mean': [72 + 8 * np.sin(i/20) + np.random.normal(0, 1.5) for i in range(200)],
        'hr_std': [4.0 + 1.0 * np.cos(i/15) + np.random.normal(0, 0.2) for i in range(200)],
        'rmssd': [45 + 12 * np.sin(i/25) + np.random.normal(0, 2) for i in range(200)],
        'stress_level': [0.3 + 0.35 * np.sin(i/30) + np.random.normal(0, 0.05) for i in range(200)],
        'fatigue_level': [0.2 + 0.25 * np.cos(i/35) + np.random.normal(0, 0.03) for i in range(200)]
    }
    pd.DataFrame(hrv_data).to_csv('sample_hrv_data.csv', index=False)
    print("✅ Created sample_hrv_data.csv with 200 samples")
    
    # 3. WESAD Data - Stress detection
    wesad_data = {
        'timestamp': timestamps,
        'eda': [3.0 + 3.5 * np.sin(i/18) + np.random.normal(0, 0.4) for i in range(200)],
        'bvp': [80 + 25 * np.cos(i/15) + np.random.normal(0, 4) for i in range(200)],
        'temp': [36.5 + 1.0 * np.sin(i/40) + np.random.normal(0, 0.15) for i in range(200)],
        'stress_label': [1 if (i % 25) > 12 else 0 for i in range(200)],
        'emotion_label': ['stress' if (i % 25) > 12 else 'calm' for i in range(200)]
    }
    pd.DataFrame(wesad_data).to_csv('sample_wesad_data.csv', index=False)
    print("✅ Created sample_wesad_data.csv with 200 samples")
    
    # 4. DEAP Data - Emotional dimensions
    deap_data = {
        'timestamp': timestamps,
        'valence': [0.5 + 0.4 * np.sin(i/20) + np.random.normal(0, 0.08) for i in range(200)],
        'arousal': [0.5 + 0.4 * np.cos(i/25) + np.random.normal(0, 0.08) for i in range(200)],
        'dominance': [0.5 + 0.3 * np.sin(i/30) + np.random.normal(0, 0.06) for i in range(200)],
        'eeg_engagement': [0.5 + 0.3 * np.cos(i/15) + np.random.normal(0, 0.05) for i in range(200)]
    }
    pd.DataFrame(deap_data).to_csv('sample_deap_data.csv', index=False)
    print("✅ Created sample_deap_data.csv with 200 samples")
    
    print("\n🎉 All 4 sample datasets created successfully!")
    print("📊 Each dataset contains 200 samples")
    print("📁 Files created in current directory:")
    print("   - sample_eeg_data.csv")
    print("   - sample_hrv_data.csv")
    print("   - sample_wesad_data.csv")
    print("   - sample_deap_data.csv")
    print("\n🚀 Now run: python app.py")

if __name__ == "__main__":
    sample_datasets()