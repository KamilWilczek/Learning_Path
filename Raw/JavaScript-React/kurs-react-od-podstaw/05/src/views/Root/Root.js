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
    twitter: [],
    article: [],
    note: [],
    isModalOpen: false,
  };

  addItem = (e, newItem) => {
    e.preventDefault();

    this.setState(prevState => ({
      [newItem.type]: [prevState[newItem.type], newItem],
    }));

    this.closeModal();
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
// 2. przywrócic funkcjonowanie addItem - O.K.
// 3. dopasować Form.js do nowych potrzeb - O.K.
// 4. przystosować widoki podstron do nowych itemów
// 5. wyświetlać odpowiednie notatki na podstronach