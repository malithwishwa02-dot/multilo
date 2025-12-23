from quantum_warmup_profile_v2 import QuantumWarmup

def run_warmup(profile_data, minutes, headless, target):
    """
    Runs the warmup session using QuantumWarmup.
    """
    print(f"[WARMUP] Initializing warmup for target: {target}")
    
    # Initialize QuantumWarmup
    # We ignore profile_data for now as QuantumWarmup generates its own driver config
    # in the original code, but we pass the parameters.
    warmup = QuantumWarmup(warmup_minutes=minutes, headless=headless, mil_integrated=True)
    
    # Inject the target into the warmup list so it's visited
    if target:
        if not target.startswith('http'):
            # Simple heuristic to add protocol
            target = f"https://{target}"
            
        print(f"[WARMUP] Adding primary target to rotation: {target}")
        warmup.TARGET_SITES.insert(0, target)
        # Give it higher probability by adding it multiple times? 
        # The logic in execute_warmup uses random.choice(site_pool), so adding it multiple times helps.
        warmup.TARGET_SITES.append(target)
        warmup.TARGET_SITES.append(target)
        
    warmup.execute_warmup()
