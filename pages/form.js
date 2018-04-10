import React from 'react';
const serverDest  = process.env.PRODUCTION ? 
  "http://127.0.0.1:5000/api/v1/input" :
  "ayobi-api/herokuapp.com/api/v1/input";

class FitnessForm extends React.Component {
  constructor(props) {
    super(props);

    this.onChange = this.onChange.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
  }

  onChange(e) {
    const name = e.target.name;
    this.setState({[name]: e.target.value});
  }

  onSubmit(e) {
    e.preventDefault();
    console.log(JSON.stringify(this.state));
    fetch(serverDest, {
      method: 'post',
      mode: 'no-cors',
      body: JSON.stringify(this.state),
      headers: {
        'content-type': 'application/json',
      },
    });
  }

  render() {
    return (<div><form onSubmit={this.onSubmit}>
      Age: <input type="number" min="13" max="110" name="age" onChange={this.onChange.bind(this)} required/><br/>
      Gender: <input list="genders" name="gender" onChange={this.onChange} required/><br/>
      Weight: <input type="number" min="0" placeholder="Kilograms" name="weight" onChange={this.onChange} required/><br/>
      Height: <input type="number" min="0" placeholder="Meters" name="height" onChange={this.onChange} required/><br/>
      Fitness: <input list="levels" name="fitness_level" onChange={this.onChange} required/><br/>
      <input type="submit"/>
      <datalist id="levels">
      <option value="low"/>
      <option value="mid"/>
      <option value="high"/>
      </datalist>
      <datalist id="genders">
      <option value="male"/>
      <option value="female"/>
      <option value="other"/>
      </datalist>
      </form>
      <iframe style={{display:"none"}} id="dummy" name="dummy"></iframe>
      </div>);
  }
}

export default FitnessForm;
