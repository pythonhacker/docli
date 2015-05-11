# -*- coding: utf-8 -*-

import click
from base_request import DigitalOcean, print_table

from urls import ACCOUNT_INFO


@click.group()
def account_group():
	"""
	account command group
	"""
	pass


@account_group.group()
def account():
	"""
	manage digital ocean account
	"""


@account.command()
@click.option('--token', '-t', type=str, help='digital ocean authentication token', metavar='<token>')
@click.option('--tablefmt', '-f', type=click.Choice(['fancy_grid', 'simple', 'plain', 'grid', 'pipe', 'orgtbl', 'psql', 'rst', 'mediawiki', 'html', 'latex', 'latex_booktabs', 'tsv']), help='output table format', default='fancy_grid', metavar='<format>')
@click.option('--proxy', '-p', help='proxy url to be used for this call', metavar='<http://ip:port>')
def info(token, tablefmt, proxy):
	"""
	get digital ocean account info
	"""
	method = 'GET'
	url = ACCOUNT_INFO
	result = DigitalOcean.do_request(method, url, token=token, proxy=proxy)
	headers = ['Fields', 'Values']
	table = []
	for key in result['account'].keys():
		table.append([key, result['account'][key]])
	data = {'headers': headers, 'table_data': table}
	print_table(tablefmt, data)