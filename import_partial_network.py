def import_partial_network(network,pretrained_model_path):
    """load every elements of the pretrained network if possible, if not do nothing"""
    """return the network with the new parameters or None if it fails"""
    if pretrained_model_path != None:

        if os.path.exists(pretrained_model_path):

            pretrained_dict = torch.load(pretrained_model_path)
            model_dict = network.state_dict()

            pretrained_dict = {k: v for k, v in pretrained_dict.items() if k in model_dict}

            for k in model_dict:
                if k not in pretrained_dict:
                    pretrained_dict[k] = model_dict[k]

            model_dict.update(pretrained_dict)
            network.load_state_dict(pretrained_dict)
            return network

        else:
            return None
