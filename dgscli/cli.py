import click
import dgscli.generator as g


@click.group()
def cli():
    pass


@click.command()
@click.option(
    "--data",
    help="Choose the dummy data: orders, products, users",
)
@click.option("--num", default=5, help="Number of records")
@click.option(
    "--no_userid",
    default=5,
    help="Number of user_id for orders",
)
@click.option(
    "--no_productid",
    default=5,
    help="Number of product_id for orders",
)
def generate(data, num, no_userid, no_productid):
    if data not in ["orders", "products", "users"]:
        raise ValueError(
            f'Your dataset "{data}" is not existed in our system! Please chooose another one'
        )
    if data == "orders":
        g.order(num, no_productid, no_userid)
        g.product(no_productid)
        g.user(no_userid)
    if data == "products":
        g.product(num)
    if data == "users":
        g.user(num)
    click.echo(f"Generated dummy data: {data} - {num}")


@click.command()
def testcommand():
    click.echo("Test command")


cli.add_command(generate)
cli.add_command(testcommand)


if __name__ == "__main__":
    cli()
