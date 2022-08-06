import click
import yaml

from runner import Runner


@click.command()
@click.option("--path-to-config", type=str)
def main(path_to_config: str):
    with open(path_to_config, "r") as f:
        config = yaml.safe_load(f)

    runner = Runner(config)

    runner.run()

if __name__ == '__main__':
    main()
