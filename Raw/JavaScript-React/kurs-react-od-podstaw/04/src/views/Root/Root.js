import React from "react";
import "./index.css";
import { BrowserRouter, Routes, Route, } from 'react-router-dom';
import ArticlesView from "../ArticlesView/ArticlesView";
import NotesView from "../NotesView/NotesView";
import TwittersView from "../TwittersView/TwittersView";


const initialStateItems = [
  {
    image: "https://avatars.githubusercontent.com/u/810438?v=4",
    name: "Dan Abramov",
    description: "React core member",
    twitterLink: "https://twitter.com/dan_abramov"
  }
];

class Root extends React.Component {
  state = {
    items: [...initialStateItems],
  };

  addItem = e => {
    e.preventDefault();

    const newItem = {
      name: e.target[0].value,
      twitterLink: e.target[1].value,
      image: e.target[2].value,
      description: e.target[3].value
    };

    this.setState(prevState => ({
      items: [...prevState.items, newItem]
    }));

    e.target.reset();
  };

  render() {
    return (
      <BrowserRouter>
        <>
          <h1>hello world</h1>
          <Routes>
            <Route path="/" element={<TwittersView />} />
            <Route path="/articles" element={<ArticlesView />} />
            <Route path="/notes" element={<NotesView />} />
          </Routes>
        </>
      </BrowserRouter>
    );
  }
}

export default Root;
