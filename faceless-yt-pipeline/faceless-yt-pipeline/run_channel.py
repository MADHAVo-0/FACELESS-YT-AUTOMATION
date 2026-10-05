"""Entry point: python run_channel.py <geology|cosmology|facts|funny>"""
import sys
import importlib


def main():
    channel = sys.argv[1]
    mod = importlib.import_module(f"channels.{channel}")
    topic = mod.get_topic()
    # TODO: dedup -> script_gen -> voiceover -> visuals -> assemble -> upload
    print(f"[{channel}] topic: {topic}")


if __name__ == "__main__":
    main()
