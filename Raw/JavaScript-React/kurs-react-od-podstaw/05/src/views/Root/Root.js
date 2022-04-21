import React from "react";
import "./index.css";
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import TwittersView from '../TwittersView/TwittersView';
import ArticlesView from '../ArticlesView/ArticlesView';
import NotesView from '../NotesView/NotesView';
import Header from '../../components/Header/Header';
import Modal from '../../components/Modal/Modal';
import AppContext from "../../context";


class Root extends React.Component {
  state = {
    items: {
      twitters: [],
      articles: [],
      notes: [],
    },
    isModalOpen: false,
  };

  addItem = e => {
    e.preventDefault();

    console.log('it works!')

    // const newItem = {
    //   name: e.target[0].value,
    //   twitterLink: e.target[1].value,
    //   image: e.target[2].value,
    //   description: e.target[3].value
    // };

    // this.setState(prevState => ({
    //   items: [...prevState.items, newItem]
    // }));

    // e.target.reset();
  };

  openModal = () => {
    this.setState({
      isModalOpen: true,
    })
  }

  closeModal = () => {
    this.setState({
      isModalOpen: false,
    })
  }

  render() {
    const { isModalOpen } = this.state;
    const contextElemnts = {
      ...this.state,
      addItem: this.addItem
    }

    return (
      <BrowserRouter>
        <AppContext.Provider value={contextElemnts}>
          <Header openModalFn={this.openModal} />
          <h1>hello world</h1>
          <Routes>
            <Route path="/" element={<TwittersView />} />
            <Route path="/articles" element={<ArticlesView />} />
            <Route path="/notes" element={<NotesView />} />
          </Routes>
          {isModalOpen && <Modal closeModalFn={this.closeModal} />}
        </AppContext.Provider>
      </BrowserRouter>
    );
  }
}

export default Root;


// Todos:
// 1. usunąć initialStateItems - O.K.
// 2. przywrócic funkcjonowanie addItem
// 3. dopasować Form.js do nowych potrzeb
// 4. przystosować widoki podstron do nowych itemów
// 5. wyświetlać odpowiednie notatki na podstronach