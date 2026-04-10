# QNECS: Quantum-Neuro Evolutionary Consciousness Simulator
# ENHANCED VERSION with SELECTABLE REAL DATASET INTEGRATION
# NOW WITH PERSONALIZED BRAIN HEALTH ASSESSMENT

import dash
from dash import dcc, html, Input, Output, State
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random
import os
import warnings
warnings.filterwarnings('ignore')

print("🚀 Starting QNECS with SELECTABLE Dataset Integration...")

# =============================================================================
# 1. REAL DATASET LOADER WITH ACTUAL DATA FILES
# =============================================================================

class RealDatasetLoader:
    """Loads and processes real physiological and emotional datasets"""
    
    def __init__(self):
        self.datasets = {}
        self.current_index = {}
        self.data_quality = {}
        
    def load_eeg_data(self, file_path='sample_eeg_data.csv'):
        """Load real EEG data from CSV file"""
        try:
            if os.path.exists(file_path):
                self.datasets['eeg'] = pd.read_csv(file_path)
                self.datasets['eeg']['timestamp'] = pd.to_datetime(self.datasets['eeg']['timestamp'])
                self.current_index['eeg'] = 0
                self.data_quality['eeg'] = 'high'
                print(f"✅ EEG Data Loaded: {len(self.datasets['eeg'])} samples")
                return True
            else:
                print("❌ EEG data file not found, using simulated data")
                return self._create_simulated_eeg_data()
        except Exception as e:
            print(f"❌ Error loading EEG data: {e}")
            return self._create_simulated_eeg_data()
    
    def load_hrv_data(self, file_path='sample_hrv_data.csv'):
        """Load real HRV data from CSV file"""
        try:
            if os.path.exists(file_path):
                self.datasets['hrv'] = pd.read_csv(file_path)
                self.datasets['hrv']['timestamp'] = pd.to_datetime(self.datasets['hrv']['timestamp'])
                self.current_index['hrv'] = 0
                self.data_quality['hrv'] = 'high'
                print(f"✅ HRV Data Loaded: {len(self.datasets['hrv'])} samples")
                return True
            else:
                print("❌ HRV data file not found, using simulated data")
                return self._create_simulated_hrv_data()
        except Exception as e:
            print(f"❌ Error loading HRV data: {e}")
            return self._create_simulated_hrv_data()
    
    def load_wesad_data(self, file_path='sample_wesad_data.csv'):
        """Load real WESAD stress data from CSV file"""
        try:
            if os.path.exists(file_path):
                self.datasets['wesad'] = pd.read_csv(file_path)
                self.datasets['wesad']['timestamp'] = pd.to_datetime(self.datasets['wesad']['timestamp'])
                self.current_index['wesad'] = 0
                self.data_quality['wesad'] = 'high'
                print(f"✅ WESAD Data Loaded: {len(self.datasets['wesad'])} samples")
                return True
            else:
                print("❌ WESAD data file not found, using simulated data")
                return self._create_simulated_wesad_data()
        except Exception as e:
            print(f"❌ Error loading WESAD data: {e}")
            return self._create_simulated_wesad_data()
    
    def load_deap_data(self, file_path='sample_deap_data.csv'):
        """Load real DEAP emotional data from CSV file"""
        try:
            if os.path.exists(file_path):
                self.datasets['deap'] = pd.read_csv(file_path)
                self.datasets['deap']['timestamp'] = pd.to_datetime(self.datasets['deap']['timestamp'])
                self.current_index['deap'] = 0
                self.data_quality['deap'] = 'high'
                print(f"✅ DEAP Data Loaded: {len(self.datasets['deap'])} samples")
                return True
            else:
                print("❌ DEAP data file not found, using simulated data")
                return self._create_simulated_deap_data()
        except Exception as e:
            print(f"❌ Error loading DEAP data: {e}")
            return self._create_simulated_deap_data()
    
    def _create_simulated_eeg_data(self):
        """Create simulated EEG data as fallback"""
        timestamps = [datetime.now() - timedelta(seconds=i) for i in range(100, 0, -1)]
        data = {
            'timestamp': timestamps,
            'alpha_power': [0.4 + 0.3 * np.sin(i/10) + random.uniform(-0.1, 0.1) for i in range(100)],
            'beta_power': [0.3 + 0.2 * np.sin(i/8) + random.uniform(-0.1, 0.1) for i in range(100)],
            'theta_power': [0.2 + 0.1 * np.sin(i/12) + random.uniform(-0.1, 0.1) for i in range(100)],
            'gamma_power': [0.1 + 0.05 * np.sin(i/15) + random.uniform(-0.05, 0.05) for i in range(100)]
        }
        self.datasets['eeg'] = pd.DataFrame(data)
        self.current_index['eeg'] = 0
        self.data_quality['eeg'] = 'simulated'
        return True
    
    def _create_simulated_hrv_data(self):
        """Create simulated HRV data as fallback"""
        timestamps = [datetime.now() - timedelta(seconds=i) for i in range(100, 0, -1)]
        data = {
            'timestamp': timestamps,
            'hr_mean': [70 + 10 * np.sin(i/20) + random.uniform(-5, 5) for i in range(100)],
            'hr_std': [4 + 2 * np.sin(i/15) + random.uniform(-1, 1) for i in range(100)],
            'rmssd': [35 + 15 * np.sin(i/25) + random.uniform(-5, 5) for i in range(100)],
            'stress_level': [0.3 + 0.4 * np.sin(i/30) + random.uniform(-0.1, 0.1) for i in range(100)],
            'fatigue_level': [0.2 + 0.3 * np.sin(i/35) + random.uniform(-0.1, 0.1) for i in range(100)]
        }
        self.datasets['hrv'] = pd.DataFrame(data)
        self.current_index['hrv'] = 0
        self.data_quality['hrv'] = 'simulated'
        return True
    
    def _create_simulated_wesad_data(self):
        """Create simulated WESAD data as fallback"""
        timestamps = [datetime.now() - timedelta(seconds=i) for i in range(100, 0, -1)]
        data = {
            'timestamp': timestamps,
            'eda': [3.0 + 3.0 * np.sin(i/25) + random.uniform(-0.5, 0.5) for i in range(100)],
            'bvp': [80 + 30 * np.sin(i/20) + random.uniform(-10, 10) for i in range(100)],
            'temp': [36.5 + 0.8 * np.sin(i/30) + random.uniform(-0.2, 0.2) for i in range(100)],
            'stress_label': [1 if (i % 30) > 15 else 0 for i in range(100)],
            'emotion_label': ['stress' if (i % 30) > 15 else 'calm' for i in range(100)]
        }
        self.datasets['wesad'] = pd.DataFrame(data)
        self.current_index['wesad'] = 0
        self.data_quality['wesad'] = 'simulated'
        return True
    
    def _create_simulated_deap_data(self):
        """Create simulated DEAP data as fallback"""
        timestamps = [datetime.now() - timedelta(seconds=i) for i in range(100, 0, -1)]
        data = {
            'timestamp': timestamps,
            'valence': [0.5 + 0.4 * np.sin(i/15) + random.uniform(-0.1, 0.1) for i in range(100)],
            'arousal': [0.5 + 0.4 * np.sin(i/18) + random.uniform(-0.1, 0.1) for i in range(100)],
            'dominance': [0.5 + 0.3 * np.sin(i/20) + random.uniform(-0.1, 0.1) for i in range(100)],
            'eeg_engagement': [0.5 + 0.3 * np.sin(i/12) + random.uniform(-0.1, 0.1) for i in range(100)]
        }
        self.datasets['deap'] = pd.DataFrame(data)
        self.current_index['deap'] = 0
        self.data_quality['deap'] = 'simulated'
        return True
    
    def get_realtime_data(self, dataset_type):
        """Get next data point from the specified dataset"""
        if dataset_type not in self.datasets or dataset_type not in self.current_index:
            return None
        
        df = self.datasets[dataset_type]
        idx = self.current_index[dataset_type]
        
        if idx >= len(df):
            # Loop back to beginning for continuous data stream
            self.current_index[dataset_type] = 0
            idx = 0
        
        data_point = df.iloc[idx].to_dict()
        self.current_index[dataset_type] += 1
        
        return data_point
    
    def get_dataset_info(self):
        """Get information about loaded datasets"""
        info = {}
        for dataset_type, df in self.datasets.items():
            info[dataset_type] = {
                'samples': len(df),
                'quality': self.data_quality.get(dataset_type, 'unknown'),
                'columns': list(df.columns),
                'current_index': self.current_index.get(dataset_type, 0)
            }
        return info

# =============================================================================
# 1.5 PERSONALIZED BRAIN HEALTH ASSESSMENT
# =============================================================================

class PersonalizedAssessment:
    """Handles personalized brain health assessment through questionnaires"""
    
    def __init__(self):
        self.user_data = {}
        self.assessment_results = {}
        
    def collect_user_data(self, name, age, responses):
        """Store user data and questionnaire responses"""
        self.user_data = {
            'name': name,
            'age': age,
            'timestamp': datetime.now(),
            'responses': responses
        }
        return self.analyze_responses(responses)
    
    def analyze_responses(self, responses):
        """Analyze questionnaire responses and generate brain health metrics"""
        # Calculate scores for different domains (0-1 scale)
        emotional_score = self.calculate_emotional_wellbeing(responses)
        cognitive_score = self.calculate_cognitive_health(responses)
        lifestyle_score = self.calculate_lifestyle_factors(responses)
        stress_score = 1.0 - self.calculate_stress_level(responses)  # Inverse for health
        
        # Overall brain health score (weighted average)
        overall_score = (
            emotional_score * 0.35 + 
            cognitive_score * 0.25 + 
            lifestyle_score * 0.25 + 
            stress_score * 0.15
        )
        
        # Generate personalized insights
        insights = self.generate_insights(
            emotional_score, cognitive_score, lifestyle_score, stress_score
        )
        
        # Create simulation parameters based on assessment
        simulation_params = self.generate_simulation_parameters(
            emotional_score, cognitive_score, lifestyle_score, stress_score, overall_score
        )
        
        self.assessment_results = {
            'overall_score': overall_score,
            'domain_scores': {
                'emotional': emotional_score,
                'cognitive': cognitive_score,
                'lifestyle': lifestyle_score,
                'stress': stress_score
            },
            'insights': insights,
            'simulation_params': simulation_params
        }
        
        return self.assessment_results
    
    def calculate_emotional_wellbeing(self, responses):
        """Calculate emotional wellbeing score from questionnaire"""
        emotional_questions = [0, 1, 2, 9, 10]  # Question indices for emotional health
        total = sum(responses[i] for i in emotional_questions)
        max_possible = len(emotional_questions) * 4  # 0-4 scale
        return total / max_possible
    
    def calculate_cognitive_health(self, responses):
        """Calculate cognitive health score from questionnaire"""
        cognitive_questions = [3, 4, 5, 11, 12]
        total = sum(responses[i] for i in cognitive_questions)
        max_possible = len(cognitive_questions) * 4
        return total / max_possible
    
    def calculate_lifestyle_factors(self, responses):
        """Calculate lifestyle factors score from questionnaire"""
        lifestyle_questions = [6, 7, 8, 13, 14]
        total = sum(responses[i] for i in lifestyle_questions)
        max_possible = len(lifestyle_questions) * 4
        return total / max_possible
    
    def calculate_stress_level(self, responses):
        """Calculate stress level from questionnaire"""
        stress_questions = [15, 16, 17, 18, 19]
        total = sum(responses[i] for i in stress_questions)
        max_possible = len(stress_questions) * 4
        return total / max_possible
    
    def generate_insights(self, emotional, cognitive, lifestyle, stress):
        """Generate personalized insights based on scores"""
        insights = []
        
        if emotional < 0.4:
            insights.append("Your emotional wellbeing needs attention. Consider mindfulness practices.")
        elif emotional > 0.7:
            insights.append("Great emotional balance! You're managing your feelings well.")
            
        if cognitive < 0.4:
            insights.append("Cognitive function could be improved with brain exercises and proper sleep.")
        elif cognitive > 0.7:
            insights.append("Excellent cognitive health! Keep challenging your brain.")
            
        if lifestyle < 0.4:
            insights.append("Lifestyle factors are impacting your brain health. Focus on exercise and nutrition.")
        elif lifestyle > 0.7:
            insights.append("Healthy lifestyle choices are supporting your brain health!")
            
        if stress > 0.7:  # Note: stress is inverted in the calculation
            insights.append("You're managing stress effectively.")
        else:
            insights.append("High stress levels detected. Consider stress-reduction techniques.")
            
        return insights
    
    def generate_simulation_parameters(self, emotional, cognitive, lifestyle, stress, overall_score):
        """Generate simulation parameters based on assessment results"""
        return {
            'chaos_level': 3.5 + ((1 - stress) * 0.5),  # Higher stress = more chaos
            'evolution_speed': 100 + (cognitive * 400),  # Better cognition = faster evolution
            'alpha_multiplier': 0.8 + (emotional * 0.4),  # Better emotion regulation = stable alpha
            'initial_health': 0.3 + (overall_score * 0.6)  # Overall score determines starting health
        }

# =============================================================================
# 2. CORE SIMULATION COMPONENTS
# =============================================================================

class ChaosEngine:
    """Chaos theory engine for generating complex, deterministic patterns"""
    def __init__(self, mu=3.9, x0=0.5):
        self.mu = mu
        self.x = x0
        self.history = [x0]
        
    def step(self):
        """Advance the chaos system by one step"""
        self.x = self.mu * self.x * (1 - self.x)
        self.history.append(self.x)
        if len(self.history) > 1000:
            self.history.pop(0)
        return self.x

    def set_mu(self, mu):
        """Set the chaos parameter mu"""
        self.mu = mu

class EmotionalIntelligenceModule:
    """Emotional intelligence with selectable dataset integration"""
    
    def __init__(self, data_loader):
        self.data_loader = data_loader
        self.current_emotion = "balanced"
        self.emotion_history = []
        self.brain_health = 0.75
        self.health_history = []
        self.active_dataset = None  # Track which dataset is active
        
        # Emotional state definitions
        self.emotion_thresholds = {
            'focused': {'coherence_min': 0.7, 'novelty_max': 0.3, 'energy_min': 0.5},
            'anxious': {'novelty_min': 0.7, 'energy_max': 0.4, 'chaos_min': 0.6},
            'curious': {'novelty_min': 0.6, 'energy_min': 0.7, 'coherence_max': 0.6},
            'confused': {'chaos_min': 0.8, 'coherence_max': 0.3, 'energy_min': 0.3},
            'fatigued': {'energy_max': 0.2, 'coherence_max': 0.4},
            'balanced': {}
        }
        
        self.emotional_modifiers = {
            'focused': {'alpha_multiplier': 0.8, 'chaos_influence': 0.3, 'mutation_rate': 0.01, 'health_impact': +0.02},
            'anxious': {'alpha_multiplier': 1.5, 'chaos_influence': 1.2, 'mutation_rate': 0.1, 'health_impact': -0.03},
            'curious': {'alpha_multiplier': 1.0, 'chaos_influence': 0.8, 'mutation_rate': 0.05, 'health_impact': +0.01},
            'confused': {'alpha_multiplier': 1.3, 'chaos_influence': 1.5, 'mutation_rate': 0.08, 'health_impact': -0.02},
            'fatigued': {'alpha_multiplier': 2.0, 'chaos_influence': 0.5, 'mutation_rate': 0.02, 'health_impact': -0.04},
            'balanced': {'alpha_multiplier': 1.0, 'chaos_influence': 1.0, 'mutation_rate': 0.03, 'health_impact': +0.005}
        }
        
        # DARKEST SHADES OF COLORS
        self.emotion_colors = {
            'focused': '#004d00', 'anxious': '#800000', 'curious': '#663300',
            'confused': '#330066', 'fatigued': '#333333', 'balanced': '#000066'
        }

    def set_active_dataset(self, dataset_type):
        """Set which dataset to use for emotion assessment"""
        self.active_dataset = dataset_type

    def assess_emotional_state_with_selected_data(self, coherence, novelty, energy, chaos, use_real_data=True):
        """Assess emotional state using selected dataset"""
        
        if not use_real_data or not self.active_dataset:
            # Fall back to simulated assessment
            emotion = self._simulated_assessment(coherence, novelty, energy, chaos)
        else:
            # Get data from selected dataset
            real_data = self.data_loader.get_realtime_data(self.active_dataset)
            emotion = self._assess_with_dataset(coherence, novelty, energy, chaos, real_data, self.active_dataset)
        
        # Update emotion history
        self.current_emotion = emotion
        self.emotion_history.append(emotion)
        if len(self.emotion_history) > 50:
            self.emotion_history.pop(0)
            
        return emotion

    def _assess_with_dataset(self, coherence, novelty, energy, chaos, real_data, dataset_type):
        """Assess emotion based on specific dataset type"""
        
        if not real_data:
            return self._simulated_assessment(coherence, novelty, energy, chaos)
        
        if dataset_type == 'eeg':
            return self._assess_with_eeg(coherence, novelty, energy, chaos, real_data)
        elif dataset_type == 'hrv':
            return self._assess_with_hrv(coherence, novelty, energy, chaos, real_data)
        elif dataset_type == 'wesad':
            return self._assess_with_wesad(coherence, novelty, energy, chaos, real_data)
        elif dataset_type == 'deap':
            return self._assess_with_deap(coherence, novelty, energy, chaos, real_data)
        else:
            return self._simulated_assessment(coherence, novelty, energy, chaos)

    def _assess_with_eeg(self, coherence, novelty, energy, chaos, eeg_data):
        """EEG-specific emotion assessment"""
        alpha = eeg_data.get('alpha_power', 0.5)
        beta = eeg_data.get('beta_power', 0.3)
        theta = eeg_data.get('theta_power', 0.2)
        
        # High alpha = focused/relaxed, High beta = anxious, High theta = drowsy
        if alpha > 0.6 and beta < 0.3:
            return "focused"
        elif beta > 0.5 and alpha < 0.4:
            return "anxious"
        elif theta > 0.4:
            return "fatigued"
        elif novelty > 0.6 and alpha > 0.5:
            return "curious"
        else:
            return "balanced"

    def _assess_with_hrv(self, coherence, novelty, energy, chaos, hrv_data):
        """HRV-specific emotion assessment"""
        stress = hrv_data.get('stress_level', 0.5)
        fatigue = hrv_data.get('fatigue_level', 0.5)
        rmssd = hrv_data.get('rmssd', 30)
        
        # Low HRV (high stress) = anxious, High fatigue = fatigued
        if stress > 0.7:
            return "anxious"
        elif fatigue > 0.6:
            return "fatigued"
        elif rmssd > 50 and stress < 0.3:  # High HRV variability = focused
            return "focused"
        elif novelty > 0.5 and stress < 0.4:
            return "curious"
        else:
            return "balanced"

    def _assess_with_wesad(self, coherence, novelty, energy, chaos, wesad_data):
        """WESAD-specific emotion assessment"""
        stress_label = wesad_data.get('stress_label', 0)
        emotion_label = wesad_data.get('emotion_label', 'calm')
        eda = wesad_data.get('eda', 3.0)
        
        if stress_label == 1 or emotion_label == 'stress':
            return "anxious"
        elif eda > 5.0:  # High electrodermal activity = arousal/stress
            return "anxious"
        elif eda < 2.5 and emotion_label == 'calm':
            return "focused"
        else:
            return "balanced"

    def _assess_with_deap(self, coherence, novelty, energy, chaos, deap_data):
        """DEAP-specific emotion assessment"""
        valence = deap_data.get('valence', 0.5)
        arousal = deap_data.get('arousal', 0.5)
        dominance = deap_data.get('dominance', 0.5)
        
        # Russell's circumplex model
        if valence > 0.7 and arousal > 0.6:
            return "focused"
        elif valence < 0.3 and arousal > 0.6:
            return "anxious"
        elif valence > 0.6 and arousal < 0.4:
            return "balanced"
        elif arousal < 0.3:
            return "fatigued"
        elif dominance < 0.3 and arousal > 0.5:
            return "confused"
        else:
            return "balanced"

    def _simulated_assessment(self, coherence, novelty, energy, chaos):
        """Fallback simulated assessment"""
        if (coherence >= self.emotion_thresholds['focused']['coherence_min'] and 
            novelty <= self.emotion_thresholds['focused']['novelty_max'] and
            energy >= self.emotion_thresholds['focused']['energy_min']):
            return "focused"
        elif (novelty >= self.emotion_thresholds['anxious']['novelty_min'] and 
              energy <= self.emotion_thresholds['anxious']['energy_max'] and
              chaos >= self.emotion_thresholds['anxious']['chaos_min']):
            return "anxious"
        elif (novelty >= self.emotion_thresholds['curious']['novelty_min'] and 
              energy >= self.emotion_thresholds['curious']['energy_min'] and
              coherence <= self.emotion_thresholds['curious']['coherence_max']):
            return "curious"
        elif (chaos >= self.emotion_thresholds['confused']['chaos_min'] and 
              coherence <= self.emotion_thresholds['confused']['coherence_max']):
            return "confused"
        elif energy <= self.emotion_thresholds['fatigued']['energy_max']:
            return "fatigued"
        else:
            return "balanced"

    def update_brain_health_with_selected_data(self, metrics, use_real_data=True):
        """Update brain health using selected dataset"""
        
        base_health = self._calculate_base_health(metrics)
        
        if not use_real_data or not self.active_dataset:
            real_health_adjustment = 0.5  # Neutral
        else:
            real_data = self.data_loader.get_realtime_data(self.active_dataset)
            real_health_adjustment = self._calculate_health_from_dataset(real_data, self.active_dataset)
        
        # Combine health scores (70% simulation, 30% real data when available)
        health_score = 0.7 * base_health + 0.3 * real_health_adjustment
        
        # Update with smoothing
        self.brain_health = np.clip(0.95 * self.brain_health + 0.05 * health_score, 0.1, 1.0)
        self.health_history.append(self.brain_health)
        if len(self.health_history) > 100:
            self.health_history.pop(0)
            
        return self.brain_health

    def _calculate_health_from_dataset(self, real_data, dataset_type):
        """Calculate health adjustment from specific dataset"""
        if not real_data:
            return 0.5
        
        if dataset_type == 'eeg':
            alpha = real_data.get('alpha_power', 0.5)
            beta = real_data.get('beta_power', 0.3)
            # Balanced EEG = better health
            return 1 - abs(alpha - 0.5) - abs(beta - 0.3)
            
        elif dataset_type == 'hrv':
            stress = real_data.get('stress_level', 0.5)
            rmssd = real_data.get('rmssd', 30)
            # Low stress + high HRV = better health
            return (1 - stress) * (min(rmssd, 100) / 100)
            
        elif dataset_type == 'wesad':
            stress_label = real_data.get('stress_label', 0)
            # No stress = better health
            return 1.0 if stress_label == 0 else 0.3
            
        elif dataset_type == 'deap':
            valence = real_data.get('valence', 0.5)
            # Positive valence = better health
            return valence
            
        return 0.5

    def _calculate_base_health(self, metrics):
        """Calculate base health from simulation metrics"""
        optimal_ranges = {
            'coherence': (0.6, 0.9), 'novelty': (0.3, 0.7),
            'energy': (0.4, 0.8), 'complexity': (0.4, 0.8)
        }
        
        health_score = 0
        for metric, value in metrics.items():
            if metric in optimal_ranges:
                low, high = optimal_ranges[metric]
                if low <= value <= high:
                    health_score += 1
                else:
                    distance = min(abs(value - low), abs(value - high))
                    health_score += max(0, 1 - distance * 2)
        
        return health_score / len(optimal_ranges)

    def get_emotional_modifiers(self):
        return self.emotional_modifiers.get(self.current_emotion, self.emotional_modifiers['balanced'])

    def get_emotion_color(self):
        return self.emotion_colors.get(self.current_emotion, '#000066')

    def get_active_dataset_info(self):
        """Get information about currently active dataset"""
        if not self.active_dataset:
            return "No dataset selected"
        return f"Active: {self.active_dataset.upper()}"

# =============================================================================
# 3. ENHANCED SIMULATION WITH SELECTABLE DATA INTEGRATION
# =============================================================================

class EnhancedQNECSSimulator:
    def __init__(self, n_nodes=40, dt=0.1, alpha=0.01):
        self.n_nodes = n_nodes
        self.dt = dt
        self.alpha = alpha
        
        # Initialize real data loader
        self.data_loader = RealDatasetLoader()
        
        # Initialize personalized assessment
        self.personalized_assessment = PersonalizedAssessment()
        
        # Load all datasets
        self.data_loader.load_eeg_data()
        self.data_loader.load_hrv_data()
        self.data_loader.load_wesad_data()
        self.data_loader.load_deap_data()
        
        self.reset()

    def complex_activation(self, z):
        magnitude = np.tanh(np.abs(z))
        phase = np.angle(z)
        return magnitude * np.exp(1j * phase)
    
    def reset(self):
        self.time = 0
        self.psi = np.random.normal(0, 0.1, self.n_nodes) + 1j * np.random.normal(0, 0.1, self.n_nodes)
        self.W = np.random.normal(scale=0.1, size=(self.n_nodes, self.n_nodes))
        np.fill_diagonal(self.W, 0)
        
        self.psi_history = [np.copy(self.psi)]
        self.chaos_engine = ChaosEngine()
        
        # Initialize emotional intelligence with selectable data
        self.emotional_module = EmotionalIntelligenceModule(self.data_loader)
        
        # Enhanced logging with dataset-specific data
        self.log = {
            'time': [], 'mean_magnitude': [], 'chaos_value': [],
            'coherence_index': [], 'novelty_index': [], 'energy_index': [],
            'complexity_index': [], 'emergence_score': [],
            'emotion': [], 'brain_health': [], 'active_dataset': [],
            'dataset_value': [], 'data_quality': []
        }
        
        print("🧠 Enhanced Simulator Reset with SELECTABLE Dataset Integration")

    def compute_complexity(self, psi):
        magnitudes = np.abs(psi)
        if np.sum(magnitudes) > 0:
            fft_vals = np.fft.fft(magnitudes)
            spectral_entropy = -np.sum(np.abs(fft_vals)**2 * np.log(np.abs(fft_vals)**2 + 1e-10))
            return np.clip(spectral_entropy / self.n_nodes, 0, 1)
        return 0.5

    def step(self, gen_interval=100, use_real_data=True, selected_dataset=None):
        # Set active dataset
        self.emotional_module.set_active_dataset(selected_dataset if use_real_data else None)
        
        # Get real data from selected dataset
        real_data = None
        if use_real_data and selected_dataset:
            real_data = self.data_loader.get_realtime_data(selected_dataset)

        # Chaos injection influenced by selected dataset
        chaos_value = self.chaos_engine.step()
        
        # Modify chaos based on selected dataset
        if real_data and selected_dataset:
            if selected_dataset == 'hrv':
                stress_level = real_data.get('stress_level', 0.5)
                chaos_value = chaos_value * (0.5 + stress_level)
            elif selected_dataset == 'wesad':
                stress_label = real_data.get('stress_label', 0)
                chaos_value = chaos_value * (1.0 if stress_label == 1 else 0.8)
        
        chaos_indices = np.random.choice(self.n_nodes, max(1, self.n_nodes//5), replace=False)
        self.psi[chaos_indices] *= np.exp(1j * np.pi * chaos_value * 0.5)

        # Neural update with dataset influence
        net_input = self.W.T @ self.psi
        self.psi = self.complex_activation(net_input) * np.exp(-self.alpha * self.dt)

        # Apply dataset-specific influence
        if real_data and selected_dataset:
            if selected_dataset == 'eeg':
                eeg_influence = real_data.get('alpha_power', 0.5) * 0.2
                influence_indices = np.random.choice(self.n_nodes, max(1, self.n_nodes//10), replace=False)
                self.psi[influence_indices] *= (1 + eeg_influence - 0.5)

        # Calculate metrics
        energy = np.clip(np.sum(np.abs(self.psi)**2) / self.n_nodes, 0, 1)
        coherence = np.clip(1 - (np.var(np.angle(self.psi)) / np.pi), 0, 1)
        
        if len(self.psi_history) > 1:
            novelty = np.clip(np.linalg.norm(np.abs(self.psi) - np.abs(self.psi_history[-1])) / np.sqrt(self.n_nodes), 0, 1)
        else:
            novelty = 0.5
            
        complexity = self.compute_complexity(self.psi)
        emergence = np.clip((novelty + coherence + complexity) / 3, 0, 1)
        
        self.psi_history.append(np.copy(self.psi))
        if len(self.psi_history) > 20:
            self.psi_history.pop(0)

        # Emotional intelligence with SELECTED dataset
        emotion = self.emotional_module.assess_emotional_state_with_selected_data(
            coherence, novelty, energy, chaos_value, use_real_data
        )
        
        # Update brain health with SELECTED dataset
        health_metrics = {
            'coherence': coherence, 'novelty': novelty, 
            'energy': energy, 'complexity': complexity
        }
        brain_health = self.emotional_module.update_brain_health_with_selected_data(health_metrics, use_real_data)
        
        # Get emotional modifiers and apply them
        modifiers = self.emotional_module.get_emotional_modifiers()
        self.alpha *= modifiers['alpha_multiplier']
        
        # Evolution influenced by selected dataset
        if self.time > 0 and self.time % gen_interval == 0:
            mutation_rate = modifiers['mutation_rate']
            
            # Dataset-specific mutation influences
            if real_data and selected_dataset:
                if selected_dataset == 'hrv':
                    stress_bonus = real_data.get('stress_level', 0) * 0.5
                    mutation_rate *= (1 + stress_bonus)
                elif selected_dataset == 'wesad':
                    if real_data.get('stress_label', 0) == 1:
                        mutation_rate *= 1.3
                
            mutation_mask = np.random.random(size=self.W.shape) < mutation_rate
            mutation_values = np.random.normal(scale=0.1, size=self.W.shape)
            self.W[mutation_mask] += mutation_values[mutation_mask]
            np.clip(self.W, -1.0, 1.0, out=self.W)

        # Enhanced logging with dataset-specific data
        self.time += 1
        self.log['time'].append(self.time)
        self.log['mean_magnitude'].append(np.mean(np.abs(self.psi)))
        self.log['chaos_value'].append(chaos_value)
        self.log['coherence_index'].append(coherence)
        self.log['novelty_index'].append(novelty)
        self.log['energy_index'].append(energy)
        self.log['complexity_index'].append(complexity)
        self.log['emergence_score'].append(emergence)
        self.log['emotion'].append(emotion)
        self.log['brain_health'].append(brain_health)
        self.log['active_dataset'].append(selected_dataset if use_real_data else 'simulation')
        
        # Store dataset-specific value for visualization
        if real_data and selected_dataset:
            if selected_dataset == 'eeg':
                self.log['dataset_value'].append(real_data.get('alpha_power', 0.5))
            elif selected_dataset == 'hrv':
                self.log['dataset_value'].append(real_data.get('stress_level', 0.5))
            elif selected_dataset == 'wesad':
                self.log['dataset_value'].append(real_data.get('eda', 3.0) / 6.0)  # Normalize
            elif selected_dataset == 'deap':
                self.log['dataset_value'].append(real_data.get('valence', 0.5))
        else:
            self.log['dataset_value'].append(0.5)
        
        self.log['data_quality'].append(self.data_loader.data_quality.get(selected_dataset, 'simulated') if selected_dataset else 'simulated')

        return True

# =============================================================================
# 4. DASH APPLICATION WITH DATASET SELECTION
# =============================================================================

app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server
sim = EnhancedQNECSSimulator(n_nodes=35)

# UI Components
def create_metric_card(title, value, color="primary", icon="📊"):
    return html.Div([
        html.Div([
            html.H6(icon, style={'fontSize': '24px', 'marginBottom': '5px', 'fontWeight': 'bold'}),
            html.H6(title, style={'fontSize': '12px', 'marginBottom': '5px', 'fontWeight': 'bold'}),
            html.H4(f"{value}", style={'fontSize': '18px', 'fontWeight': 'bold'})
        ], style={"padding": "15px", "textAlign": "center", "height": "100%"})
    ], className=f"card text-white bg-{color} mb-3", style={"height": "120px", "borderRadius": "10px"})

def create_control_card(title, children, icon="⚙️"):
    return html.Div([
        html.Div([
            html.H5(f"{icon} {title}", style={"marginBottom": "15px", "color": "#000000", "fontWeight": "bold"}),
            *children
        ], style={"padding": "20px"})
    ], className="card", style={"marginBottom": "20px", "borderRadius": "10px"})

def create_emotion_indicator(emotion, color, dataset_info=""):
    return html.Div([
        html.Div([
            html.H4("Current Emotional State", style={'textAlign': 'center', 'marginBottom': '10px', 'color': '#000000', 'fontWeight': 'bold'}),
            html.Div([
                html.H2(emotion.upper(), style={
                    'textAlign': 'center', 'color': color, 'fontWeight': 'bold',
                    'fontSize': '28px', 'textShadow': '2px 2px 4px rgba(0,0,0,0.1)'
                }),
                html.P(dataset_info, style={
                    'textAlign': 'center', 'color': '#333333', 'fontSize': '12px', 'marginTop': '5px', 'fontWeight': 'bold'
                }) if dataset_info else None
            ], style={
                'padding': '20px', 'background': 'linear-gradient(135deg, #f8f9fa, #e9ecef)',
                'borderRadius': '15px', 'border': f'3px solid {color}'
            })
        ])
    ], className="card", style={"padding": "15px", "marginBottom": "20px", "borderRadius": "10px"})

# Application Layout
app.layout = html.Div([
    html.Div([
        html.Div([
            html.H1("🧠 QNECS: Quantum-Neuro Evolutionary Consciousness Simulator", 
                    style={'textAlign': 'center', 'color': 'white', 'marginBottom': '10px', 'fontWeight': 'bold'}),
            html.P("SELECTABLE Real Dataset Integration + Personalized Brain Health Assessment", 
                   style={'textAlign': 'center', 'color': 'rgba(255,255,255,0.8)', 'fontSize': '18px', 'fontWeight': 'bold'})
        ])
    ], style={
        'background': 'linear-gradient(135deg, #004d00 0%, #000066 100%)',
        'padding': '30px', 'marginBottom': '30px', 'borderRadius': '0 0 20px 20px'
    }),
    
    html.Div([
        # Left Control Panel
        html.Div([
            create_control_card("🎮 Simulation Controls", [
                html.Button('🚀 START SIMULATION', id='start-button', n_clicks=0, 
                           className='btn btn-success btn-block', 
                           style={'marginBottom': '10px', 'padding': '12px', 'fontWeight': 'bold'}),
                html.Button('⏸️ PAUSE', id='pause-button', n_clicks=0, 
                           className='btn btn-warning btn-block', 
                           style={'marginBottom': '10px', 'padding': '12px', 'fontWeight': 'bold'}),
                html.Button('🔄 RESET SYSTEM', id='reset-button', n_clicks=0, 
                           className='btn btn-danger btn-block', 
                           style={'marginBottom': '20px', 'padding': '12px', 'fontWeight': 'bold'}),
                html.Hr(),
                html.Div(id='status-display', children=[
                    html.H4("Status: READY", style={'color': '#800000', 'textAlign': 'center', 'fontWeight': 'bold'})
                ])
            ]),
            
            create_control_card("📊 Dataset Selection", [
                html.Label("🎛️ Choose Data Source", style={'fontWeight': 'bold', 'marginBottom': '10px'}),
                dcc.Dropdown(
                    id='dataset-selector',
                    options=[
                        {'label': ' 🧠 EEG Data (Brain Waves)', 'value': 'eeg'},
                        {'label': ' 💓 HRV Data (Heart Rate Variability)', 'value': 'hrv'},
                        {'label': ' 📈 WESAD Data (Stress Detection)', 'value': 'wesad'},
                        {'label': ' 🎭 DEAP Data (Emotional Dimensions)', 'value': 'deap'},
                        {'label': ' 🧪 Simulation Only (No Real Data)', 'value': 'simulation'},
                        {'label': ' 👤 Personalized Assessment', 'value': 'personalized'}  # NEW OPTION
                    ],
                    value='eeg',
                    style={'marginBottom': '15px'}
                ),
                html.Div(id='dataset-description', style={
                    'padding': '10px', 'backgroundColor': '#f8f9fa', 
                    'borderRadius': '5px', 'fontSize': '12px', 'marginTop': '10px', 'fontWeight': 'bold'
                }),
                html.Hr(),
                html.Label("🌐 Data Integration Mode", style={'fontWeight': 'bold', 'marginTop': '10px'}),
                dcc.RadioItems(
                    id='real-data-toggle',
                    options=[
                        {'label': ' 🔌 Real Data OFF', 'value': 'simulation'},
                        {'label': ' 💡 Real Data ON', 'value': 'real_data'}
                    ],
                    value='real_data',
                    style={'marginTop': '10px'}
                )
            ]),
            
            html.Div(id='emotion-display-container'),
            
            create_control_card("❤️ Brain Health Monitor", [
                html.Div(id='brain-health-gauge', style={'textAlign': 'center'}),
                dcc.Graph(id='health-trend', config={'displayModeBar': False}, 
                         style={'height': '150px', 'marginTop': '10px'})
            ]),
            
            create_control_card("⚡ System Parameters", [
                html.Label("🧠 Chaos Level", style={'fontWeight': 'bold'}),
                dcc.Slider(id='chaos-mu-slider', min=3.5, max=4.0, step=0.01, value=3.9,
                          marks={3.5: 'Low', 3.7: 'Med', 3.9: 'High', 4.0: 'Max'}),
                
                html.Label("🔄 Evolution Speed", style={'fontWeight': 'bold', 'marginTop': '20px'}),
                dcc.Slider(id='gen-interval-slider', min=50, max=500, step=50, value=200,
                          marks={50: 'Fast', 200: 'Med', 500: 'Slow'})
            ])
            
        ], className="three columns", style={'padding': '10px'}),
        
        # Right Visualization Panel
        html.Div([
            # First Row
            html.Div([
                html.Div([
                    html.H4("🌐 Neural Network Activity", 
                           style={'textAlign': 'center', 'color': '#000000', 'marginBottom': '15px', 'fontWeight': 'bold'}),
                    dcc.Graph(id='network-graph', style={'height': '400px'})
                ], className="card", style={'padding': '15px', 'height': '450px', 'borderRadius': '10px'}),
                
                html.Div([
                    html.H4("📈 Emotional Timeline", 
                           style={'textAlign': 'center', 'color': '#000000', 'marginBottom': '15px', 'fontWeight': 'bold'}),
                    dcc.Graph(id='emotional-timeline', style={'height': '400px'})
                ], className="card", style={'padding': '15px', 'height': '450px', 'borderRadius': '10px'})
            ], className="row", style={'marginBottom': '20px'}),
            
            # Second Row
            html.Div([
                html.Div([
                    html.H4("📊 Brain Metrics & Dataset Correlation", 
                           style={'textAlign': 'center', 'color': '#000000', 'marginBottom': '15px', 'fontWeight': 'bold'}),
                    dcc.Graph(id='metrics-plot', style={'height': '350px'})
                ], className="card", style={'padding': '15px', 'height': '400px', 'borderRadius': '10px'}),
                
                html.Div([
                    html.H4("📡 Selected Dataset Stream", 
                           style={'textAlign': 'center', 'color': '#000000', 'marginBottom': '15px', 'fontWeight': 'bold'}),
                    dcc.Graph(id='dataset-plot', style={'height': '350px'})
                ], className="card", style={'padding': '15px', 'height': '400px', 'borderRadius': '10px'})
            ], className="row", style={'marginBottom': '20px'}),
            
            # Third Row
            html.Div([
                html.Div([
                    html.H4("🎯 Live Metrics & Dataset Info", 
                           style={'textAlign': 'center', 'color': '#000000', 'marginBottom': '15px', 'fontWeight': 'bold'}),
                    html.Div(id='live-metrics', className="row"),
                    html.Div(id='active-dataset-info', style={
                        'marginTop': '15px', 'padding': '10px', 'backgroundColor': '#f8f9fa',
                        'borderRadius': '5px', 'textAlign': 'center', 'fontWeight': 'bold'
                    })
                ], className="card", style={'padding': '20px', 'borderRadius': '10px'})
            ], className="row")
            
        ], className="nine columns", style={'padding': '10px'})
    ], className="row"),
    
    # Questionnaire Modal
    html.Div([
        html.Div([
            html.Div([
                html.H3("🧠 Personalized Brain Health Assessment", 
                       style={'textAlign': 'center', 'color': '#000000', 'marginBottom': '20px', 'fontWeight': 'bold'}),
                
                # Basic Information
                html.Div([
                    html.H5("Personal Information", style={'color': '#000000', 'marginBottom': '15px', 'fontWeight': 'bold'}),
                    html.Div([
                        html.Div([
                            html.Label("Full Name *", style={'fontWeight': 'bold'}),
                            dcc.Input(id='user-name', type='text', placeholder='Enter your name', 
                                     style={'width': '100%', 'padding': '8px', 'marginBottom': '15px'})
                        ], className="six columns"),
                        html.Div([
                            html.Label("Age *", style={'fontWeight': 'bold'}),
                            dcc.Input(id='user-age', type='number', placeholder='Enter your age',
                                     style={'width': '100%', 'padding': '8px', 'marginBottom': '15px'})
                        ], className="six columns")
                    ], className="row")
                ], style={'marginBottom': '25px'}),
                
                # Questionnaire
                html.Div([
                    html.H5("Brain Health Questionnaire", 
                           style={'color': '#000000', 'marginBottom': '15px', 'fontWeight': 'bold'}),
                    html.P("Rate each statement from 0 (Never) to 4 (Always)", 
                          style={'color': '#333333', 'fontSize': '14px', 'marginBottom': '20px', 'fontWeight': 'bold'})
                ]),
                
                # Questions - Emotional Wellbeing
                html.Div([
                    html.H6("Emotional Wellbeing", style={'color': '#004d00', 'marginBottom': '10px', 'fontWeight': 'bold'}),
                    *[
                        html.Div([
                            html.Label(f"{i+1}. {question}", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                            dcc.Slider(
                                id=f'q{i}', min=0, max=4, step=1, value=2,
                                marks={0: 'Never', 1: 'Rarely', 2: 'Sometimes', 3: 'Often', 4: 'Always'},
                                tooltip={"placement": "bottom", "always_visible": True}
                            )
                        ], style={'marginBottom': '20px'})
                        for i, question in enumerate([
                            "I feel generally happy and content",
                            "I can manage my emotions effectively",
                            "I feel motivated and engaged",
                            "My memory and recall are sharp",
                            "I can concentrate for extended periods",
                            "I learn new things easily",
                            "I get 7-9 hours of quality sleep nightly",
                            "I exercise regularly (3+ times/week)",
                            "I maintain a balanced, nutritious diet",
                            "I have meaningful social connections",
                            "I feel optimistic about the future",
                            "I can solve problems creatively",
                            "I maintain a consistent daily routine",
                            "I take regular breaks during work",
                            "I engage in hobbies and relaxation",
                            "I feel overwhelmed by responsibilities",
                            "I experience physical tension or headaches",
                            "I have trouble switching off at night",
                            "I feel irritable or impatient frequently",
                            "I worry about things beyond my control"
                        ])
                    ]
                ]),
                
                # Buttons
                html.Div([
                    html.Button('Submit Assessment', id='submit-assessment', 
                               className='btn btn-success', 
                               style={'marginRight': '10px', 'padding': '10px 20px', 'fontWeight': 'bold'}),
                    html.Button('Cancel', id='cancel-assessment', 
                               className='btn btn-secondary',
                               style={'padding': '10px 20px', 'fontWeight': 'bold'})
                ], style={'textAlign': 'center', 'marginTop': '30px'})
                
            ], style={'padding': '30px', 'maxHeight': '80vh', 'overflowY': 'auto'})
        ], style={
            'backgroundColor': 'white', 
            'borderRadius': '15px',
            'boxShadow': '0 10px 30px rgba(0,0,0,0.3)',
            'width': '90%',
            'maxWidth': '800px',
            'margin': '5% auto'
        })
    ], id='questionnaire-modal', style={
        'display': 'none',
        'position': 'fixed',
        'zIndex': 1000,
        'left': 0,
        'top': 0,
        'width': '100%',
        'height': '100%',
        'backgroundColor': 'rgba(0,0,0,0.5)'
    }),
    
    dcc.Interval(id='interval-component', interval=500, n_intervals=0, disabled=True),
    dcc.Store(id='simulation-state', data={'running': False}),
    dcc.Store(id='selected-dataset', data='eeg'),
    
], style={'backgroundColor': '#f8f9fa', 'minHeight': '100vh'})

# =============================================================================
# 5. CALLBACKS FOR DATASET SELECTION
# =============================================================================

@app.callback(
    Output('dataset-description', 'children'),
    [Input('dataset-selector', 'value')]
)
def update_dataset_description(selected_dataset):
    """Update description based on selected dataset"""
    descriptions = {
        'eeg': "🧠 EEG Data: Measures brain electrical activity. Alpha waves indicate relaxation, Beta waves indicate focus/anxiety.",
        'hrv': "💓 HRV Data: Heart Rate Variability measures autonomic nervous system. Low HRV indicates stress, high HRV indicates relaxation.",
        'wesad': "📈 WESAD Data: Wearable stress detection using EDA (electrodermal activity), BVP (blood volume pulse), and temperature.",
        'deap': "🎭 DEAP Data: Emotional dimensions - Valence (pleasure), Arousal (intensity), Dominance (control).",
        'simulation': "🧪 Simulation Only: Using purely simulated data without real physiological input.",
        'personalized': "👤 Personalized Assessment: Complete a questionnaire for customized brain health analysis and simulation parameters."
    }
    return html.Div(descriptions.get(selected_dataset, "Select a dataset to see description."), style={'fontWeight': 'bold'})

@app.callback(
    Output('selected-dataset', 'data'),
    [Input('dataset-selector', 'value')]
)
def update_selected_dataset(selected_dataset):
    """Store the selected dataset"""
    return selected_dataset

@app.callback(
    [Output('interval-component', 'disabled'),
     Output('status-display', 'children')],
    [Input('start-button', 'n_clicks'),
     Input('pause-button', 'n_clicks'),
     Input('reset-button', 'n_clicks')],
    [State('simulation-state', 'data')]
)
def control_simulation(start_clicks, pause_clicks, reset_clicks, state):
    ctx = dash.callback_context
    if not ctx.triggered:
        return True, html.H4("Status: READY", style={'color': '#800000', 'textAlign': 'center', 'fontWeight': 'bold'})
    
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if button_id == 'start-button':
        return False, html.H4("Status: RUNNING", style={'color': '#004d00', 'textAlign': 'center', 'fontWeight': 'bold'})
    elif button_id == 'pause-button':
        return True, html.H4("Status: PAUSED", style={'color': '#663300', 'textAlign': 'center', 'fontWeight': 'bold'})
    elif button_id == 'reset-button':
        sim.reset()
        return True, html.H4("Status: RESET", style={'color': '#800000', 'textAlign': 'center', 'fontWeight': 'bold'})
    
    return True, html.H4("Status: READY", style={'color': '#800000', 'textAlign': 'center', 'fontWeight': 'bold'})

@app.callback(
    Output('simulation-state', 'data'),
    [Input('start-button', 'n_clicks'),
     Input('pause-button', 'n_clicks'),
     Input('reset-button', 'n_clicks')],
    [State('simulation-state', 'data')]
)
def update_simulation_state(start_clicks, pause_clicks, reset_clicks, state):
    ctx = dash.callback_context
    if not ctx.triggered:
        return {'running': False}
    
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if button_id == 'start-button':
        return {'running': True}
    elif button_id == 'pause-button':
        return {'running': False}
    elif button_id == 'reset-button':
        return {'running': False}
    
    return state

# =============================================================================
# 6. CALLBACKS FOR PERSONALIZED ASSESSMENT
# =============================================================================

@app.callback(
    Output('questionnaire-modal', 'style'),
    [Input('dataset-selector', 'value'),
     Input('cancel-assessment', 'n_clicks'),
     Input('submit-assessment', 'n_clicks')],
    [State('questionnaire-modal', 'style')]
)
def toggle_questionnaire_modal(selected_dataset, cancel_clicks, submit_clicks, current_style):
    ctx = dash.callback_context
    if not ctx.triggered:
        return current_style
    
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if trigger_id == 'dataset-selector' and selected_dataset == 'personalized':
        return {'display': 'block', 'position': 'fixed', 'zIndex': 1000, 
                'left': 0, 'top': 0, 'width': '100%', 'height': '100%', 
                'backgroundColor': 'rgba(0,0,0,0.5)'}
    elif trigger_id in ['cancel-assessment', 'submit-assessment']:
        return {'display': 'none'}
    
    return current_style

@app.callback(
    [Output('status-display', 'children', allow_duplicate=True),
     Output('simulation-state', 'data', allow_duplicate=True),
     Output('selected-dataset', 'data', allow_duplicate=True)],
    [Input('submit-assessment', 'n_clicks')],
    [State('user-name', 'value'),
     State('user-age', 'value'),
     State('simulation-state', 'data')] +
    [State(f'q{i}', 'value') for i in range(20)],  # All 20 questions
    prevent_initial_call=True
)
def process_assessment(submit_clicks, name, age, sim_state, *responses):
    if not submit_clicks or not name or not age:
        raise dash.exceptions.PreventUpdate
    
    # Extract responses
    responses = list(responses)
    
    # Validate all responses are provided
    if any(r is None for r in responses):
        return [
            html.H4("Please answer all questions!", 
                   style={'color': '#800000', 'textAlign': 'center', 'fontWeight': 'bold'}),
            sim_state,
            'personalized'
        ]
    
    # Process assessment
    assessment_results = sim.personalized_assessment.collect_user_data(name, age, responses)
    
    # Apply personalized parameters to simulation
    params = assessment_results['simulation_params']
    sim.chaos_engine.set_mu(params['chaos_level'])
    sim.emotional_module.brain_health = params['initial_health']
    
    return [
        html.H4("Assessment Complete! Running Personalized Simulation", 
               style={'color': '#004d00', 'textAlign': 'center', 'fontWeight': 'bold'}),
        {'running': True},
        'personalized'
    ]

@app.callback(
    [Output('network-graph', 'figure'),
     Output('emotional-timeline', 'figure'),
     Output('metrics-plot', 'figure'),
     Output('dataset-plot', 'figure'),
     Output('emotion-display-container', 'children'),
     Output('brain-health-gauge', 'children'),
     Output('health-trend', 'figure'),
     Output('live-metrics', 'children'),
     Output('active-dataset-info', 'children')],
    [Input('interval-component', 'n_intervals'),
     Input('reset-button', 'n_clicks')],
    [State('chaos-mu-slider', 'value'),
     State('gen-interval-slider', 'value'),
     State('real-data-toggle', 'value'),
     State('selected-dataset', 'data'),
     State('simulation-state', 'data')]
)
def update_all_visualizations(n_intervals, reset_clicks, chaos_mu, gen_interval, real_data_mode, selected_dataset, sim_state):
    ctx = dash.callback_context
    
    if ctx.triggered and ctx.triggered[0]['prop_id'] == 'reset-button.n_clicks':
        return get_empty_visualizations()
    
    if sim_state['running'] and n_intervals > 0:
        sim.chaos_engine.set_mu(chaos_mu)
        use_real_data = (real_data_mode == 'real_data')
        # Only use dataset if real data is enabled and not simulation-only
        dataset_to_use = selected_dataset if (use_real_data and selected_dataset != 'simulation') else None
        sim.step(gen_interval=gen_interval, use_real_data=use_real_data, selected_dataset=dataset_to_use)
    
    return create_all_visualizations(sim, selected_dataset, real_data_mode)

def get_empty_visualizations():
    """Return empty visualizations for reset state"""
    empty_fig = go.Figure()
    empty_fig.update_layout(
        xaxis=dict(visible=False), yaxis=dict(visible=False),
        annotations=[dict(text="System Reset - Click START", showarrow=False, font=dict(weight='bold'))],
        plot_bgcolor='rgba(240,240,240,0.1)'
    )
    
    emotion_display = create_emotion_indicator("READY", "#333333", "No dataset selected")
    health_gauge = create_health_gauge(0.75)
    health_trend = create_health_trend([])
    live_metrics = create_live_metrics_empty()
    dataset_info = html.Div("Select a dataset and click START", style={'color': '#333333', 'fontWeight': 'bold'})
    
    return [empty_fig] * 4 + [emotion_display, health_gauge, health_trend, live_metrics, dataset_info]

def create_all_visualizations(sim, selected_dataset, real_data_mode):
    """Create all visualizations based on selected dataset"""
    network_fig = create_network_visualization(sim, selected_dataset)
    timeline_fig = create_emotional_timeline(sim, selected_dataset)
    metrics_fig = create_metrics_plot(sim, selected_dataset)
    dataset_fig = create_dataset_plot(sim, selected_dataset)
    
    # Emotion display with dataset info
    current_emotion = sim.emotional_module.current_emotion if sim.log['emotion'] else "READY"
    emotion_color = sim.emotional_module.get_emotion_color()
    
    if selected_dataset == 'personalized':
        dataset_info = "Personalized Assessment Mode"
    elif real_data_mode == 'real_data' and selected_dataset != 'simulation':
        dataset_info = f"Using: {selected_dataset.upper()} Data"
    else:
        dataset_info = "Simulation Only Mode"
    
    emotion_display = create_emotion_indicator(current_emotion, emotion_color, dataset_info)
    
    # Brain health
    brain_health = sim.emotional_module.brain_health if sim.log['brain_health'] else 0.75
    health_gauge = create_health_gauge(brain_health)
    health_trend = create_health_trend(sim.emotional_module.health_history)
    
    # Live metrics and dataset info
    live_metrics = create_live_metrics(sim, selected_dataset)
    
    # Active dataset info
    if selected_dataset == 'personalized':
        if hasattr(sim.personalized_assessment, 'user_data') and sim.personalized_assessment.user_data:
            user_name = sim.personalized_assessment.user_data.get('name', 'User')
            dataset_info = html.Div([
                html.Strong(f"Personalized Assessment: {user_name}"),
                html.Br(),
                html.Span("Custom simulation based on questionnaire responses", 
                         style={'color': '#333333', 'fontSize': '12px', 'fontWeight': 'bold'})
            ])
        else:
            dataset_info = html.Div([
                html.Strong("Personalized Assessment Ready"),
                html.Br(),
                html.Span("Complete the questionnaire to start", style={'color': '#333333', 'fontSize': '12px', 'fontWeight': 'bold'})
            ])
    elif real_data_mode == 'real_data' and selected_dataset != 'simulation':
        dataset_quality = sim.data_loader.data_quality.get(selected_dataset, 'unknown')
        dataset_samples = len(sim.data_loader.datasets.get(selected_dataset, []))
        dataset_info = html.Div([
            html.Strong(f"Active Dataset: {selected_dataset.upper()}"),
            html.Br(),
            html.Span(f"Quality: {dataset_quality} • Samples: {dataset_samples}", 
                     style={'color': '#333333', 'fontSize': '12px', 'fontWeight': 'bold'})
        ])
    else:
        dataset_info = html.Div([
            html.Strong("Mode: Simulation Only"),
            html.Br(),
            html.Span("No real data integration", style={'color': '#333333', 'fontSize': '12px', 'fontWeight': 'bold'})
        ])
    
    return network_fig, timeline_fig, metrics_fig, dataset_fig, emotion_display, health_gauge, health_trend, live_metrics, dataset_info

# Visualization functions with dataset-specific adaptations
def create_network_visualization(sim, selected_dataset):
    """Create neural network visualization with dataset influence"""
    node_magnitudes = np.abs(sim.psi)
    
    fig = go.Figure()
    
    # Simulate node positions
    node_x = np.random.normal(0, 1, sim.n_nodes)
    node_y = np.random.normal(0, 1, sim.n_nodes)
    
    fig.add_trace(go.Scatter(
        x=node_x, y=node_y, 
        mode='markers',
        marker=dict(
            size=15 + node_magnitudes * 25,
            color=node_magnitudes,
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title='Activation', title_font=dict(weight='bold'), tickfont=dict(weight='bold'))
        ),
        text=[f'Node {i}: {mag:.3f}' for i, mag in enumerate(node_magnitudes)],
        hoverinfo='text'
    ))
    
    # Add dataset influence indicator
    if selected_dataset == 'personalized' and hasattr(sim.personalized_assessment, 'assessment_results'):
        health_score = sim.personalized_assessment.assessment_results['overall_score']
        fig.add_annotation(
            x=0.02, y=0.98, xref="paper", yref="paper",
            text=f"Personalized Health: {health_score:.2f}",
            showarrow=False,
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
            font=dict(weight='bold')
        )
    elif sim.log['dataset_value']:
        current_value = sim.log['dataset_value'][-1]
        dataset_names = {
            'eeg': 'EEG Alpha', 'hrv': 'HRV Stress', 
            'wesad': 'WESAD EDA', 'deap': 'DEAP Valence'
        }
        value_name = dataset_names.get(selected_dataset, 'Data')
        
        fig.add_annotation(
            x=0.02, y=0.98, xref="paper", yref="paper",
            text=f"{value_name}: {current_value:.3f}",
            showarrow=False,
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
            font=dict(weight='bold')
        )
    
    title = "Neural Network Activity"
    if selected_dataset == 'personalized':
        title += " + Personalized Assessment"
    elif selected_dataset != 'simulation':
        title += f" + {selected_dataset.upper()} Influence"
    
    fig.update_layout(
        title=dict(text=title, font=dict(weight='bold', size=16)),
        showlegend=False,
        margin=dict(b=20,l=20,r=20,t=40),
        height=400,
        plot_bgcolor='rgba(240,240,240,0.1)',
        font=dict(weight='bold')
    )
    return fig

def create_emotional_timeline(sim, selected_dataset):
    """Create emotional timeline with dataset correlation"""
    if len(sim.log['time']) < 2:
        return create_empty_plot("Collecting data...")
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Emotional states
    emotion_map = {'focused': 4, 'curious': 3, 'balanced': 2, 'fatigued': 1, 'anxious': 0, 'confused': -1}
    emotion_values = [emotion_map.get(e, 0) for e in sim.log['emotion']]
    
    fig.add_trace(go.Scatter(
        x=sim.log['time'], y=emotion_values,
        mode='lines+markers', name='Emotion',
        line=dict(color='#000066', width=3)
    ), secondary_y=False)
    
    # Dataset values overlay or personalized health
    if selected_dataset == 'personalized' and hasattr(sim.personalized_assessment, 'assessment_results'):
        health_score = sim.personalized_assessment.assessment_results['overall_score']
        fig.add_hline(y=health_score * 4, line_dash="dash", line_color="#663300", 
                     annotation_text=f"Personalized Health Baseline", annotation_font=dict(weight='bold'))
    
    elif any(sim.log['dataset_value']) and selected_dataset != 'simulation':
        fig.add_trace(go.Scatter(
            x=sim.log['time'], y=sim.log['dataset_value'],
            mode='lines', name=f'{selected_dataset.upper()} Data',
            line=dict(color='#800000', width=2, dash='dash')
        ), secondary_y=True)
    
    fig.update_layout(
        title=dict(text="Emotional Timeline" + (f" + {selected_dataset.upper()} Correlation" if selected_dataset not in ['simulation', 'personalized'] else " + Personalized Assessment"), font=dict(weight='bold', size=16)),
        xaxis_title="Time Step",
        height=400,
        plot_bgcolor='rgba(240,240,240,0.1)',
        font=dict(weight='bold'),
        legend=dict(font=dict(weight='bold'))
    )
    fig.update_xaxes(title_font=dict(weight='bold'), tickfont=dict(weight='bold'))
    fig.update_yaxes(title_text="Emotional State", secondary_y=False, title_font=dict(weight='bold'), tickfont=dict(weight='bold'))
    if selected_dataset != 'simulation' and selected_dataset != 'personalized':
        fig.update_yaxes(title_text=f"{selected_dataset.upper()} Value", secondary_y=True, title_font=dict(weight='bold'), tickfont=dict(weight='bold'))
    
    return fig

def create_metrics_plot(sim, selected_dataset):
    """Create metrics plot showing simulation and dataset correlation"""
    if len(sim.log['time']) < 2:
        return create_empty_plot("Collecting data...")
    
    fig = go.Figure()
    
    # Simulation metrics
    fig.add_trace(go.Scatter(
        x=sim.log['time'], y=sim.log['coherence_index'],
        mode='lines', name='Coherence',
        line=dict(color='#004d00', width=2)
    ))
    
    fig.add_trace(go.Scatter(
        x=sim.log['time'], y=sim.log['emergence_score'],
        mode='lines', name='Emergence',
        line=dict(color='#330066', width=2)
    ))
    
    # Dataset correlation or personalized assessment
    if selected_dataset == 'personalized' and hasattr(sim.personalized_assessment, 'assessment_results'):
        # Show personalized health score
        health_score = sim.personalized_assessment.assessment_results['overall_score']
        fig.add_hline(y=health_score, line_dash="dash", line_color="#663300", 
                     annotation_text=f"Personalized Health: {health_score:.2f}", annotation_font=dict(weight='bold'))
    
    elif any(sim.log['dataset_value']) and selected_dataset != 'simulation':
        fig.add_trace(go.Scatter(
            x=sim.log['time'], y=sim.log['dataset_value'],
            mode='lines', name=f'{selected_dataset.upper()} Data',
            line=dict(color='#663300', width=2, dash='dot')
        ))
    
    title = "Brain Metrics"
    if selected_dataset == 'personalized':
        title += " + Personalized Assessment"
    elif selected_dataset != 'simulation':
        title += f" + {selected_dataset.upper()} Correlation"
    
    fig.update_layout(
        title=dict(text=title, font=dict(weight='bold', size=16)),
        xaxis_title="Time Step",
        yaxis_title="Metric Value",
        height=350,
        plot_bgcolor='rgba(240,240,240,0.1)',
        font=dict(weight='bold'),
        legend=dict(font=dict(weight='bold'))
    )
    fig.update_xaxes(title_font=dict(weight='bold'), tickfont=dict(weight='bold'))
    fig.update_yaxes(title_font=dict(weight='bold'), tickfont=dict(weight='bold'))
    return fig

def create_dataset_plot(sim, selected_dataset):
    """Create dataset-specific visualization"""
    if len(sim.log['time']) < 2 or selected_dataset == 'simulation':
        return create_empty_plot("Select a dataset and enable real data mode")
    
    if selected_dataset == 'personalized':
        # Create personalized assessment results visualization
        if not hasattr(sim.personalized_assessment, 'assessment_results') or not sim.personalized_assessment.assessment_results:
            return create_empty_plot("Complete the questionnaire to see personalized results")
        
        fig = go.Figure()
        
        # Radar chart for domain scores
        domains = list(sim.personalized_assessment.assessment_results['domain_scores'].keys())
        scores = list(sim.personalized_assessment.assessment_results['domain_scores'].values())
        
        fig.add_trace(go.Scatterpolar(
            r=scores + [scores[0]],  # Close the radar
            theta=domains + [domains[0]],  # Close the radar
            fill='toself',
            name='Domain Scores',
            line=dict(color='#000066')
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 1], tickfont=dict(weight='bold'))
            ),
            showlegend=False,
            title=dict(text="Personalized Brain Health Domains", font=dict(weight='bold', size=16)),
            height=350,
            font=dict(weight='bold')
        )
        return fig
    
    fig = go.Figure()
    
    if any(sim.log['dataset_value']):
        # Plot the dataset values with appropriate styling
        colors = {'eeg': '#000066', 'hrv': '#800000', 'wesad': '#663300', 'deap': '#330066'}
        color = colors.get(selected_dataset, '#333333')
        
        fig.add_trace(go.Scatter(
            x=sim.log['time'], y=sim.log['dataset_value'],
            mode='lines+markers',
            name=f'{selected_dataset.upper()} Data Stream',
            line=dict(color=color, width=3),
            marker=dict(size=4, color=color)
        ))
    
    # Add dataset-specific reference lines or annotations
    if selected_dataset == 'eeg':
        fig.add_hline(y=0.6, line_dash="dash", line_color="#004d00", annotation_text="High Alpha", annotation_font=dict(weight='bold'))
        fig.add_hline(y=0.4, line_dash="dash", line_color="#800000", annotation_text="High Beta", annotation_font=dict(weight='bold'))
    elif selected_dataset == 'hrv':
        fig.add_hline(y=0.7, line_dash="dash", line_color="#800000", annotation_text="High Stress", annotation_font=dict(weight='bold'))
        fig.add_hline(y=0.3, line_dash="dash", line_color="#004d00", annotation_text="Low Stress", annotation_font=dict(weight='bold'))
    
    fig.update_layout(
        title=dict(text=f"{selected_dataset.upper()} Data Stream", font=dict(weight='bold', size=16)),
        xaxis_title="Time Step",
        yaxis_title="Data Value",
        height=350,
        plot_bgcolor='rgba(240,240,240,0.1)',
        font=dict(weight='bold'),
        legend=dict(font=dict(weight='bold'))
    )
    fig.update_xaxes(title_font=dict(weight='bold'), tickfont=dict(weight='bold'))
    fig.update_yaxes(title_font=dict(weight='bold'), tickfont=dict(weight='bold'))
    return fig

def create_empty_plot(message):
    """Create an empty plot with a message"""
    fig = go.Figure()
    fig.update_layout(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        annotations=[dict(
            text=message,
            showarrow=False,
            xref="paper", yref="paper",
            x=0.5, y=0.5, xanchor='center', yanchor='middle',
            font=dict(weight='bold', size=14)
        )],
        plot_bgcolor='rgba(240,240,240,0.1)'
    )
    return fig

def create_health_gauge(health_score):
    """Create brain health gauge"""
    color = '#004d00' if health_score > 0.7 else '#663300' if health_score > 0.4 else '#800000'
    return html.Div([
        html.Div(f"{health_score:.1%}", style={
            "fontSize": "32px", "fontWeight": "bold", "color": color,
            "textAlign": "center", "marginBottom": "10px"
        }),
        html.Div("Brain Health Score", style={"textAlign": "center", "color": "#333333", "fontWeight": "bold"}),
        html.Div([
            html.Div(style={
                "width": f"{health_score*100}%", "height": "10px", "backgroundColor": color,
                "borderRadius": "5px", "marginTop": "10px"
            })
        ], style={
            "width": "100%", "backgroundColor": "#ecf0f1", "borderRadius": "5px"
        })
    ])

def create_health_trend(health_history):
    """Create health trend visualization"""
    if len(health_history) < 2:
        return create_empty_plot("Health data collecting...")
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        y=[h * 100 for h in health_history],
        mode='lines',
        line=dict(color='#004d00', width=3)
    ))
    
    fig.update_layout(
        showlegend=False,
        margin=dict(l=0, r=0, t=0, b=0),
        height=150,
        plot_bgcolor='rgba(240,240,240,0.1)',
        yaxis=dict(range=[0, 100], showticklabels=False),
        xaxis=dict(showticklabels=False)
    )
    return fig

def create_live_metrics(sim, selected_dataset):
    """Create live metrics cards with dataset-specific info"""
    if not sim.log['time']:
        return create_live_metrics_empty()
    
    # Base metrics
    metrics = [
        ("Emergence", sim.log['emergence_score'][-1], "info", "🌱"),
        ("Coherence", sim.log['coherence_index'][-1], "success", "🔗"),
        ("Brain Health", sim.log['brain_health'][-1], "primary", "❤️"),
    ]
    
    # Add dataset-specific metric
    if selected_dataset == 'personalized' and hasattr(sim.personalized_assessment, 'assessment_results'):
        health_score = sim.personalized_assessment.assessment_results['overall_score']
        metrics.append(("Personalized Health", health_score, "warning", "👤"))
    elif selected_dataset != 'simulation' and sim.log['dataset_value']:
        dataset_metrics = {
            'eeg': ("EEG Alpha", sim.log['dataset_value'][-1], "warning", "🧠"),
            'hrv': ("HRV Stress", sim.log['dataset_value'][-1], "danger", "💓"),
            'wesad': ("Stress EDA", sim.log['dataset_value'][-1], "danger", "📈"),
            'deap': ("Valence", sim.log['dataset_value'][-1], "warning", "🎭")
        }
        metrics.append(dataset_metrics.get(selected_dataset, ("Data", 0.5, "secondary", "📊")))
    else:
        metrics.append(("Data Mode", 0.0, "secondary", "🧪"))
    
    return [
        html.Div(create_metric_card(title, f"{value:.2f}", color, icon), className="three columns")
        for title, value, color, icon in metrics
    ]

def create_live_metrics_empty():
    """Create empty live metrics"""
    metrics = [
        ("Emergence", "0.00", "secondary", "🌱"),
        ("Coherence", "0.00", "secondary", "🔗"),
        ("Brain Health", "0.00", "secondary", "❤️"),
        ("Dataset", "N/A", "secondary", "📊")
    ]
    
    return [
        html.Div(create_metric_card(title, value, color, icon), className="three columns")
        for title, value, color, icon in metrics
    ]

# =============================================================================
# 7. APPLICATION START
# =============================================================================

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render uses 10000 default
    app.run_server(host="0.0.0.0", port=port)
