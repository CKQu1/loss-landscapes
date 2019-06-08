import abc
import loss_landscapes.common.model_interface.model_tensor as model_tensor


class ModelWrapper(abc.ABC):
    def __init__(self, model, get_components_fn=None, forward_fn=None):
        self.model = model                            # wrapped model
        self.get_components_fn = get_components_fn    # how to get state
        self.forward_fn = forward_fn                  # how to use model in evaluation

    def get_model(self):
        """
        Return a reference to the model encapsulated in this wrapper.
        :return: wrapped model
        """
        return self.model

    @abc.abstractmethod
    def forward(self, x):
        """
        Calls the model or agent on the given inputs, and returns the desired output.
        :param x: inputs to the model or agent
        :return: model output
        """
        pass

    @abc.abstractmethod
    def get_parameters(self, deepcopy=False) -> model_tensor.ParameterTensor:
        """
        Return a ParameterTensor wrapping the parameters of the underlying model. The
        parameters can either be returned as a view of the model parameters or as a copy.
        :param deepcopy: whether to view or deepcopy the model parameters
        :return: view or deepcopy of accessible model parameters
        """
        pass

    @abc.abstractmethod
    def set_parameters(self, new_parameters: model_tensor.ParameterTensor):
        """
        Sets the parameters of the wrapped model to the given ParameterVector.
        :param new_parameters: ParameterVector of new parameters
        :return: none
        """
        pass

