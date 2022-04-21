import React from 'react';
import AppContext from '../../context';

const ArticlesView = () => (
  <AppContext.Consumer>
    {(context) => (
      <p>This is an Articles View {context}</p>
    )}
  </AppContext.Consumer>
);

export default ArticlesView;