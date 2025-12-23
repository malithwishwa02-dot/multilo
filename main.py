import argparse
from fulz_input import interactive_fulz_input, load_fulz_json
from profile_generator import generate_profile
from injector import inject_artifacts
from warmup import run_warmup
from mistral_api import ask_mistral

def main():
    parser = argparse.ArgumentParser(description="Quantum Profile Warmup CLI")
    parser.add_argument('--interactive', action='store_true', help='Stepwise FULZ/target entry')
    parser.add_argument('--fulz', type=str, help='FULZ+CC+target input JSON')
    parser.add_argument('--target', type=str, help='Target system')
    parser.add_argument('--minutes', type=int, default=30, help='Warmup session duration')
    parser.add_argument('--headless', action='store_true', help='Run browser headless')
    parser.add_argument('--mistral-api-key', type=str, default='', help='Mistral AI API key')
    parser.add_argument('--output', type=str, default='out', help='Output directory')

    args = parser.parse_args()

    # FULZ/target collection
    if args.interactive:
        fulz = interactive_fulz_input()
    elif args.fulz:
        fulz = load_fulz_json(args.fulz)
    else:
        print("Must specify --interactive or --fulz.")
        exit(1)
    if args.target:
        fulz['target'] = args.target

    # Mistral AI augment step (optional)
    if args.mistral_api_key:
        want_ai = input("Ask Mistral AI for advice/mutation? [y/N]: ").strip().lower()
        if want_ai == "y":
            prompt = input("Enter AI help prompt (or leave blank to summarize profile/task): ").strip()
            if not prompt:
                prompt = f"Given this persona:\n{fulz}\nTarget system: {fulz['target']}\nWhat tweaks or defenses should I bypass in profile/data/warmup?"
            print("Mistral AI says:\n", ask_mistral(prompt, args.mistral_api_key))

    # Profile/Artifact generation
    profile_data = generate_profile(fulz, args.output)
    inject_artifacts(profile_data, args.output)

    # Warm-up session
    run_warmup(profile_data, args.minutes, args.headless, fulz['target'])

if __name__ == '__main__':
    main()