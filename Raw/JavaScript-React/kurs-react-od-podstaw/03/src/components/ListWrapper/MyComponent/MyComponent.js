import React from 'react'

class MyComponent extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            text: ''
        }

        this.handleChange = this.handleChange.bind(this)
    }
    // ^ old way if we do not overwrite extended class constructor

    handleChange(e) {
        this.setState({ text: e.target.value.toUpperCase() })
    }

    render() {
        return (
            <>
                <input
                    placeholder='your text'
                    onChange={this.handleChange}
                    value={this.state.text}
                />
                <h1>{this.state.text}</h1>
            </>

        )
    }
}

export default MyComponent;