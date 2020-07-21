import React from 'react';
import {Container, Switch, Typography, Grid, Button, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@material-ui/core';
import {get} from '../utils/Api'

class Portfolio extends React.Component {
  constructor(props) {
    super(props);
    this.state = { 
      portfolio_type: true,
      demo_portfolio: '',
      demo_positions: [],
      pending_orders_demo: [],
      real_portfolio: '',
      real_positions: [],
      pending_orders_real: [],
    };
  }

  componentDidMount() {
    this.retrieve_portfolio()
  }

  retrieve_portfolio = async () => {
    get('api/retrieve_portfolio/').then((resp) => {
      if (resp.status === 200){
        var response = JSON.parse(resp.response)
        console.log(response)
        this.setState({
          demo_portfolio: response.p_demo.portfolio,
          demo_positions: response.p_demo.positions,
          pending_orders_demo: response.p_demo.pending_orders,
          real_portfolio: response.p_real.portfolio,
          real_positions: response.p_real.positions,
          pending_orders_real: response.p_real.pending_orders
        })
      }
    })
  }

  get_portfolio = async () => {
    get('api/update_portfolio/').then((resp) => {
        // console.log(resp)
    })
  }

  update_orders = async () => {
    get('api/update_orders/').then((resp) => {
        // console.log(resp)
    })
  }

  transmit_orders = async () => {
    get('api/transmit_orders/').then((resp) => {
        // console.log(resp)
    })
  }



  handlePortfolioChange = async (e) => {
    this.setState({portfolio_type: !this.state.portfolio_type})
  }

  renderPositions = () => {
    var positions = []
    if (this.state.portfolio_type) {
      positions = this.state.real_positions
    } else {
      positions = this.state.demo_positions
    }

    return(
      positions.map((position) => (
        <TableRow key={position.symbol}>
          <TableCell component="th" scope="row">{position.stock.symbol} </TableCell>
          <TableCell align="right">{position.invest_date}</TableCell>
          <TableCell align="right">{position.invest_value}</TableCell>
          <TableCell align="right">{position.invest_units}</TableCell>
          <TableCell align="right">{position.open_rate}</TableCell>
          <TableCell align="right">{position.current_rate}</TableCell>
          <TableCell align="right">{position.stop_loss_rate}</TableCell>
          <TableCell align="right">{position.take_profit_rate}</TableCell>
          <TableCell align="right" style={{color: position.current_rate - position.open_rate > 0 ? 'green' : 'red'}}> {position.current_rate - position.open_rate } </TableCell>
        </TableRow>
      ))
    )
  }

  renderPendingOrders = () => {
    var pending_orders = []
    if (this.state.portfolio_type) {
      pending_orders = this.state.pending_orders_real
    } else {
      pending_orders = this.state.pending_orders_demo
    }
    return(
      pending_orders.map((pending_order) => (
        <TableRow key={pending_order.id}>
          <TableCell component="th" scope="row">{pending_order.stock.symbol} </TableCell>
          <TableCell component="th" scope="row" style={{color: pending_order.sma_position.buy ? 'green' : 'red'}} >{pending_order.sma_position.buy ? 'BUY' : 'SELL'} </TableCell>
          <TableCell align="right">{Math.round(pending_order.total_investment)}</TableCell>
          <TableCell align="right">{Math.round(pending_order.num_of_shares)}</TableCell>
          <TableCell align="right">{Math.round(pending_order.order_price)}</TableCell>
          <TableCell align="right">{Math.round(pending_order.stop_loss)}</TableCell>
          <TableCell align="right">{Math.round(pending_order.take_profit)}</TableCell>
          <TableCell align="right"> {new Date(pending_order.price_date).toLocaleString()} </TableCell>
          <TableCell align="right"> {new Date(pending_order.created_at).toLocaleString()} </TableCell>
          <TableCell align="right"> {pending_order.submited_at === null ? 'Not submitted' : pending_order.submited_at} </TableCell>
          <TableCell align="right"> {pending_order.executed_at === null ? 'Not executed' : pending_order.executed_at} </TableCell>
        </TableRow>
      )))
  }

  renderPortfolio = () => {
    if (this.state.portfolio_type) {
      var portfolio = this.state.real_portfolio
    } else {
      var portfolio = this.state.demo_portfolio
    }
    return (
      <Grid container direction="row" alignItems="center" justify="center" style={{padding:10}}>
        <Typography style={{paddingRight: 10}}>
          Date: {new Date(portfolio.date).toLocaleString()}
        </Typography>
        <Typography style={{paddingRight: 10}}>
          Cash: {portfolio.cash}
        </Typography>
        <Typography>
          Total invested value: {portfolio.total_invested_value}
        </Typography>
      </Grid>
    )
  }
  render() {
    return (
      <Container>
        <Grid container direction="row" alignItems="center" justify="center">
          <Typography>
            {this.state.portfolio_type && 'Real portfolio'}
            {!this.state.portfolio_type && 'Demo portfolio'}
          </Typography>
          <Switch
            checked={this.state.portfolio_type}
            onChange={e => {this.handlePortfolioChange(e);}}
            name="portfolio_type"
            color="primary"
          />
          <Button
            type="submit"
            variant="contained"
            color="primary"
            onClick={() => {this.get_portfolio()}}
          >
            Update portfolio
          </Button>
        </Grid>
        <Grid container style={{paddingBottom: 10}} direction="column" alignItems="center" justify="center">
          {this.renderPortfolio()}
        </Grid>
        <Grid container direction="column" alignItems="center" justify="center">
            <Typography variant="h6" style={{padding: 10}}>
              Portfolio
            </Typography>
          <TableContainer component={Paper}>
            <Table aria-label="simple table">
              <TableHead>
                <TableRow>
                  <TableCell style={{fontWeight:'bold'}}>Symbol</TableCell>
                  <TableCell style={{fontWeight:'bold'}} align="right">Investment date</TableCell>
                  <TableCell style={{fontWeight:'bold'}} align="right">Invested value </TableCell>
                  <TableCell style={{fontWeight:'bold'}} align="right">Invested units</TableCell>
                  <TableCell style={{fontWeight:'bold'}} align="right">Open rate</TableCell>
                  <TableCell style={{fontWeight:'bold'}} align="right">Current rate</TableCell>
                  <TableCell style={{fontWeight:'bold'}} align="right">Stop loss</TableCell>
                  <TableCell style={{fontWeight:'bold'}} align="right">Take profit</TableCell>
                  <TableCell style={{fontWeight:'bold'}} align="right">Unrealized gain/loss</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {this.renderPositions()}
              </TableBody>
            </Table>
          </TableContainer>
          <Grid container direction="row" alignItems="center" justify="center">
            <Typography variant="h6" style={{padding: 10}}>
              Pending orders
            </Typography>
          
            <Button
              type="submit"
              variant="contained"
              color="primary"
              onClick={() => {this.update_orders()}}
              style={{margin: 10}}
            >
              Update orders
            </Button>
            <Button
              type="submit"
              variant="contained"
              color="primary"
              onClick={() => {this.transmit_orders()}}
              style={{margin: 10}}
            >
              Transmit orders
            </Button>
          </Grid>
          <TableContainer component={Paper}>
            <Table aria-label="simple table">
              <TableHead>
                <TableRow>
                  <TableCell style={{fontWeight:'bold'}}>Symbol</TableCell>
                  <TableCell style={{fontWeight:'bold'}} align="right">Order type </TableCell>
                  <TableCell style={{fontWeight:'bold'}} align="right">Invested value </TableCell>
                  <TableCell style={{fontWeight:'bold'}} align="right">Invested units</TableCell>
                  <TableCell style={{fontWeight:'bold'}} align="right">Open rate</TableCell>
                  <TableCell style={{fontWeight:'bold'}} align="right">Stop loss</TableCell>
                  <TableCell style={{fontWeight:'bold'}} align="right">Take profit</TableCell>
                  <TableCell style={{fontWeight:'bold'}} align="right">Price date</TableCell>
                  <TableCell style={{fontWeight:'bold'}} align="right">Creation date</TableCell>
                  <TableCell style={{fontWeight:'bold'}} align="right">Sent date</TableCell>
                  <TableCell style={{fontWeight:'bold'}} align="right">Execution date</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {this.renderPendingOrders()}
              </TableBody>
            </Table>
          </TableContainer>
        </Grid>
      </Container>
    ); 
  }
}

export default Portfolio