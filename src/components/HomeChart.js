import React from 'react';
import { AreaChart, Area, CartesianGrid, XAxis, YAxis, Tooltip, BarChart, LabelList, Bar, Cell } from 'recharts';
import { withStyles } from '@material-ui/core/styles';

const styles = {

}

const DataFormater = (number) => {
  if(number > 1000000000){
    return (number/1000000000).toString() + 'B';
  }else if(number > 1000000){
    return (number/1000000).toString() + 'M';
  }else if(number > 1000){
    return (number/1000).toString() + 'K';
  }else{
    return number.toFixed(1).toString();
  }
}

const PercentageFormater = (number) => {
  return number.toFixed(1) + '%'
}

class HomeChart extends React.Component {
  constructor(props) {
    super(props);
    this.state = { 

    };
  }

  render() {
    const { theme } = this.props;
    switch (this.props.graph_type) {
      case 'investments':
        return(
          <AreaChart height={this.props.height*0.82} width={this.props.width*0.98} data={this.props.data} >
            <CartesianGrid strokeDasharray="3 3"/>
            <XAxis dataKey="name" fill={this.props.theme.palette.type === 'dark' ? this.props.theme.palette.common.white : this.props.theme.palette.common.black}/>
            <YAxis tickFormatter={DataFormater} fill={this.props.theme.palette.type === 'dark' ? this.props.theme.palette.common.white : this.props.theme.palette.common.black} />
            <Tooltip />
            <Area type='monotone' dataKey='total_invested_value' stackId='1' stroke={theme.palette.type === 'dark' ? theme.palette.secondary.dark : theme.palette.secondary.light} fill={theme.palette.type === 'dark' ? theme.palette.secondary.dark : theme.palette.secondary.light} />
          </AreaChart>
        )
      case 'cash':
        return(
          <AreaChart height={this.props.height*0.82} width={this.props.width*0.98} data={this.props.data} >
            <CartesianGrid strokeDasharray="3 3"/>
            <XAxis dataKey="name" fill={this.props.theme.palette.type === 'dark' ? this.props.theme.palette.common.white : this.props.theme.palette.common.black}/>
            <YAxis tickFormatter={DataFormater} fill={this.props.theme.palette.type === 'dark' ? this.props.theme.palette.common.white : this.props.theme.palette.common.black} />
            <Tooltip />
            <Area type='monotone' dataKey='cash' stackId='1' stroke={theme.palette.type === 'dark' ? theme.palette.primary.dark : theme.palette.primary.light} fill={theme.palette.type === 'dark' ? theme.palette.primary.dark : theme.palette.primary.light} />
          </AreaChart>
        )
      case 'cash_investments':
        return(
          <AreaChart height={this.props.height*0.82} width={this.props.width*0.98} data={this.props.data} >
            <CartesianGrid strokeDasharray="3 3"/>
            <XAxis dataKey="name" fill={this.props.theme.palette.type === 'dark' ? this.props.theme.palette.common.white : this.props.theme.palette.common.black}/>
            <YAxis tickFormatter={DataFormater} fill={this.props.theme.palette.type === 'dark' ? this.props.theme.palette.common.white : this.props.theme.palette.common.black} />
            <Tooltip />
            <Area type='monotone' dataKey='total_invested_value' stackId='1' stroke={theme.palette.type === 'dark' ? theme.palette.secondary.dark : theme.palette.secondary.light} fill={theme.palette.type === 'dark' ? theme.palette.secondary.dark : theme.palette.secondary.light} />
            <Area type='monotone' dataKey='cash' stackId='1' stroke={theme.palette.type === 'dark' ? theme.palette.primary.dark : theme.palette.primary.light} fill={theme.palette.type === 'dark' ? theme.palette.primary.dark : theme.palette.primary.light} />
          </AreaChart>
        )
      case 'performance_pct':
        return(
          <BarChart height={this.props.height*0.82} width={this.props.width*0.98} data={this.props.data} >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis tickFormatter={PercentageFormater} domain={[-10,10]}/>
            <Bar dataKey="perf" >
              {this.props.data.map((entry, index) => (
                <Cell key={entry.name} fill={entry.perf > 0 ? 'green' : 'red' }/>
              ))}
              <LabelList dataKey="perf" position="top" formatter={PercentageFormater} />
          </Bar>
          </BarChart>
        )
      case 'performance_curr':
        return(
          <BarChart height={this.props.height*0.82} width={this.props.width*0.98} data={this.props.data} >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis tickFormatter={DataFormater}/>
            <Bar dataKey="diff" >
              {this.props.data.map((entry, index) => (
                <Cell key={entry.name} fill={entry.diff > 0 ? 'green' : 'red' }/>
              ))}
              <LabelList dataKey="diff" position="top" formatter={DataFormater} />
          </Bar>
          </BarChart>
        )
      default:
        break;
    }
  }
}

export default withStyles(styles, { withTheme: true })(HomeChart);
